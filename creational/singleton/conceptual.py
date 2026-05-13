from dataclasses import dataclass, field
from typing import Self


@dataclass
class Singleton:
    _instance: Self | None = field(default=None)

    def __init__(self) -> None:
        if not self._instance:
            exception = "Use get_instance() to access the Singleton instance"
            raise RuntimeError(exception)

    @classmethod
    def get_instance(cls) -> Self:
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance  # type: ignore[no-any-return]


variable = Singleton.get_instance()
another_variable = Singleton.get_instance()

print(variable is another_variable)  # True
