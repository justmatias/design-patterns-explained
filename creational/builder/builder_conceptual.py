from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Product:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    parts: list[str] = field(default_factory=list)

    def add(self, part: str) -> None:
        self.parts.append(part)


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> Product:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    _product: Product

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self._product = Product()

    @property
    def product(self) -> Product:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("Part A1")

    def produce_part_b(self) -> None:
        self._product.add("Part B1")

    def produce_part_c(self) -> None:
        self._product.add("Part C1")


@dataclass
class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    The Director can construct several product variations using the same
    building steps.
    """

    builder: Builder
    """
    The Director works with any builder instance that the client code passes
    to it. This way, the client code may alter the final type of the newly
    assembled product.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    builder = ConcreteBuilder()
    director = Director(builder)

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    print(f"Product: {builder.product}")  # Product(parts=["Part A1"])

    print("Standard full featured product: ")
    director.build_full_featured_product()
    print(builder.product)  # Product(parts=["Part A1", "Part B1", "Part C1"])

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    print(builder.product)  # Product(parts=["Part A1", "Part B1"])
