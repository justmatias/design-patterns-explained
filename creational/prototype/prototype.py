import copy
from dataclasses import dataclass
from typing import Self


class Character:
    def clone(self) -> Self:
        return copy.deepcopy(self)


@dataclass
class GameCharacter(Character):
    name: str
    level: int
    weapon: str

    def __str__(self) -> str:
        return f"{self.name} (Level {self.level}) with {self.weapon}"


# Base prototype
warrior = GameCharacter("Warrior", 1, "Sword")

# Clone to create new variations
knight = warrior.clone()
knight.name = "Knight"
knight.level = 2

paladin = warrior.clone()
paladin.name = "Paladin"
paladin.weapon = "Hammer"

print("Original: ", warrior)
print("Clone 1: ", knight)
print("Clone 2: ", paladin)
