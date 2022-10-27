from typing import TypeVar, Generic


# Scenario 1
A = TypeVar("A")
B = TypeVar("B", default=str)
C = TypeVar("C", default=float)
class Product(Generic[A, B, C]):
    def __init__(
        self,
        attr1: A,
        attr2: B,
        attr3: C,
    ):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

p1 = Product[int, str, float]
p2 = Product[int, str]
p3 = Product[int]
assert p1 == p2
assert p2 == p3