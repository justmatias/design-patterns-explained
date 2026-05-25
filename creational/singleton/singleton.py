from typing import Any, ClassVar, Self

from pydantic import BaseModel, Field


class Settings(BaseModel):
    instance: ClassVar[Self | None] = None
    settings: dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def get_settings(cls, settings: dict[str, Any]) -> Self:
        if cls.instance is None:
            cls.instance = cls(settings=settings)
        return cls.instance


settings = Settings.get_settings({"db": "postgres", "debug": True})
settings_2 = Settings.get_settings({"db": "mysql", "debug": False})

assert settings is settings_2
