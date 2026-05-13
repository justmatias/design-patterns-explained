from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import Self


class Engine(Enum):
    GAS = auto()
    DIESEL = auto()


class Chassis(Enum):
    TAXI = auto()
    SPORTS_CAR = auto()


class Color(Enum):
    RED = auto()
    YELLOW = auto()
    BLACK = auto()


@dataclass
class Car:
    engine: Engine
    chassis: Chassis
    wheels: int
    color: Color | None = Color.BLACK
    gps: bool | None = False

    def __str__(self) -> str:
        return (
            f"Car with engine: {self.engine}, chassis: {self.chassis}, "
            f"wheels: {self.wheels}, color: {self.color}, gps: {self.gps}"
        )


class CarBuilder(ABC):
    car: Car

    def build(self) -> Car:
        return self.car

    @abstractmethod
    def with_gps(self) -> Self:
        pass

    @abstractmethod
    def with_color(self, color: Color) -> Self:
        pass


class TaxiBuilder(CarBuilder):
    def __init__(self) -> None:
        self.car = Car(engine=Engine.GAS, chassis=Chassis.TAXI, wheels=4)

    def with_gps(self) -> Self:
        self.car.gps = True
        return self

    def with_color(self, color: Color) -> Self:
        self.car.color = color
        return self


class SportsCarBuilder(CarBuilder):
    def __init__(self) -> None:
        self.car = Car(engine=Engine.DIESEL, chassis=Chassis.SPORTS_CAR, wheels=4)

    def build(self) -> Car:
        return self.car

    def with_gps(self) -> Self:
        self.car.gps = True
        return self

    def with_color(self, color: Color) -> Self:
        self.car.color = color
        return self


class CarDirector:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def build_taxi(self) -> Car:
        return self.builder.with_color(Color.YELLOW).build()

    def build_sports_car(self) -> Car:
        return self.builder.with_gps().with_color(Color.RED).build()


if __name__ == "__main__":
    print("Example using director class: ")
    sports_car_builder = SportsCarBuilder()
    sports_car = CarDirector(sports_car_builder).build_sports_car()
    print(sports_car)
    print()
    print("Example using builder directly: ")
    taxi_builder = TaxiBuilder()
    taxi = taxi_builder.with_color(Color.YELLOW).build()
    print(taxi)
