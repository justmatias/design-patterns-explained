from dataclasses import dataclass, field
from typing import Any, Self


@dataclass
class Settings:
    _instance: Self | None = field(default=None)
    settings: dict[str, Any] = field(default_factory=dict)

    def __init__(self, settings: dict[str, Any]):
        if self._instance is not None:
            exception = "Use get_instance() instead of creating Settings directly"
            raise RuntimeError(exception)
        self.settings = settings or {}

    @classmethod
    def get_instance(cls, settings: dict[str, Any]) -> Self:
        if cls._instance is None:
            cls._instance = cls(settings)
        return cls._instance  # type: ignore[no-any-return]


settings = Settings.get_instance({"db": "postgres", "debug": True})
settings_2 = Settings.get_instance({"db": "mysql", "debug": False})

assert settings is settings_2
