from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    Інтерфейс Component оголошує метод `accept`, який має приймати
    базовий інтерфейс відвідувача як аргумент.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):
    """
    Кожен конкретний компонент повинен реалізовувати метод `accept` таким чином
    що він викликає метод відвідувача, який відповідає класу компонента.
    """

    def accept(self, visitor: Visitor) -> None:
        """
        Зауважте, що ми викликаємо `visitConcreteComponentA`, який відповідає
        поточній назві класу. Таким чином ми повідомляємо відвідувачу клас
        компонент, з яким він працює.
        """

        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        """
        Конкретні компоненти можуть мати спеціальні методи, яких у них немає:
        базовий клас або інтерфейс. Відвідувач все ще може використовувати ці методи
        оскільки він знає конкретний клас компонента.
        """

        return "A"


class ConcreteComponentB(Component):
    """
    Same here: visitConcreteComponentB => ConcreteComponentB
    """

    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"


class Visitor(ABC):
    """
    The Visitor Interface declares a set of visiting methods that correspond to
    component classes. The signature of a visiting method allows the visitor to
    identify the exact class of the component that it's dealing with.
    """

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass


"""
Concrete Visitors implement several versions of the same algorithm, which can
work with all concrete component classes.

You can experience the biggest benefit of the Visitor pattern when using it with
a complex object structure, such as a Composite tree. In this case, it might be
helpful to store some intermediate state of the algorithm while executing
visitor's methods over various objects of the structure.
"""


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")


def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    The client code can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    # ...
    for component in components:
        component.accept(visitor)
    # ...


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)
