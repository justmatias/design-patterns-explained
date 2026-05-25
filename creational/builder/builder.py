from abc import ABC, abstractmethod
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any, Self
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class EventType(StrEnum):
    ORDER_PLACED = "OrderPlaced"
    PAYMENT_CAPTURED = "PaymentCaptured"


class Event(BaseModel):
    event_type: EventType
    payload: dict[str, Any]
    event_id: UUID = Field(default_factory=uuid4)
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    source: str
    correlation_id: str | None = None
    causation_id: UUID | None = None
    schema_version: int = 1
    metadata: dict[str, str] = Field(default_factory=dict)

    def __str__(self) -> str:
        return (
            f"{self.event_type} (id={self.event_id}, source={self.source}, "
            f"v{self.schema_version}, correlation={self.correlation_id}, "
            f"causation={self.causation_id}, metadata={self.metadata})"
        )


class EventBuilder(ABC):
    _event: Event

    @property
    def event(self) -> Event:
        return self._event

    def build(self) -> Event:
        return self._event

    @abstractmethod
    def with_metadata(self, key: str, value: str) -> Self: ...

    @abstractmethod
    def correlated_to(self, correlation_id: str) -> Self: ...

    @abstractmethod
    def caused_by(self, prior: Event) -> Self: ...


class DomainEventBuilder(EventBuilder):
    """Builds internal events for a single bounded context."""

    def __init__(self, event_type: EventType, payload: dict[str, Any]) -> None:
        self._event = Event(
            event_type=event_type,
            payload=payload,
            source="orders-service",
        )

    def with_metadata(self, key: str, value: str) -> Self:
        self._event.metadata[key] = value
        return self

    def correlated_to(self, correlation_id: str) -> Self:
        self._event.correlation_id = correlation_id
        return self

    def caused_by(self, prior: Event) -> Self:
        self._event.causation_id = prior.event_id
        self._event.correlation_id = prior.correlation_id
        return self


class IntegrationEventBuilder(EventBuilder):
    """Builds public events shared across services, so a schema version is required."""

    def __init__(
        self, event_type: EventType, payload: dict[str, Any], schema_version: int
    ) -> None:
        self._event = Event(
            event_type=event_type,
            payload=payload,
            source="orders-service.public",
            schema_version=schema_version,
        )
        self._event.metadata["content-type"] = "application/json"

    def with_metadata(self, key: str, value: str) -> Self:
        self._event.metadata[key] = value
        return self

    def correlated_to(self, correlation_id: str) -> Self:
        self._event.correlation_id = correlation_id
        return self

    def caused_by(self, prior: Event) -> Self:
        self._event.causation_id = prior.event_id
        self._event.correlation_id = prior.correlation_id
        return self


if __name__ == "__main__":
    print("Domain event: ")
    first_event = (
        DomainEventBuilder(EventType.ORDER_PLACED, {"order_id": 42, "total": 99.90})
        .correlated_to("corr-abc-123")
        .with_metadata("trace-id", "corr-abc-123")
        .build()
    )
    print(first_event)
    print()
    print("Integration event caused by the domain event: ")
    payment_event = (
        IntegrationEventBuilder(
            EventType.PAYMENT_CAPTURED,
            {"order_id": 42, "amount": 99.90},
            schema_version=2,
        )
        .caused_by(first_event)
        .with_metadata("partition-key", "order-42")
        .build()
    )
    print(payment_event)
