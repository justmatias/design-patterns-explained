import copy
from dataclasses import dataclass
from typing import Self


class Prototype:
    def clone(self) -> Self:
        return copy.deepcopy(self)


@dataclass
class ConcretePrototype(Prototype):
    value: int

    def __str__(self) -> str:
        return f"ConcretePrototype(value={self.value})"


original = ConcretePrototype(42)
clone = original.clone()

print("Original: ", original)
print("Clone: ", clone)
print("Are objects the same?", original is clone)  # False
