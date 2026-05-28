from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self) -> str: ...


class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self) -> str: ...

    @abstractmethod
    def collaborate(self, collaborator: AbstractProductA) -> str: ...


class ConcreteProductA1(AbstractProductA):
    def operation_a(self) -> str:
        return "Result from ConcreteProductA1"


class ConcreteProductA2(AbstractProductA):
    def operation_a(self) -> str:
        return "Result from ConcreteProductA2"


class ConcreteProductB1(AbstractProductB):
    def operation_b(self) -> str:
        return "Result from ConcreteProductB1"

    def collaborate(self, collaborator: AbstractProductA) -> str:
        return f"B1 collaborating with ({collaborator.operation_a()})"


class ConcreteProductB2(AbstractProductB):
    def operation_b(self) -> str:
        return "Result from ConcreteProductB2"

    def collaborate(self, collaborator: AbstractProductA) -> str:
        return f"B2 collaborating with ({collaborator.operation_a()})"


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA: ...

    @abstractmethod
    def create_product_b(self) -> AbstractProductB: ...


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_b.operation_b())
    print(product_b.collaborate(product_a))


if __name__ == "__main__":
    print("Factory 1:")
    client_code(ConcreteFactory1())
    print("\nFactory 2:")
    client_code(ConcreteFactory2())
