from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str: ...


class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result from ConcreteProductA"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result from ConcreteProductB"


class Creator(ABC):
    @abstractmethod
    def create_product(self) -> Product: ...

    def some_operation(self) -> str:
        product = self.create_product()
        return f"Creator working with: {product.operation()}"


class ConcreteCreatorA(Creator):
    def create_product(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def create_product(self) -> Product:
        return ConcreteProductB()


if __name__ == "__main__":
    for creator in (ConcreteCreatorA(), ConcreteCreatorB()):
        print(creator.some_operation())
