#Usando a metaclass Enum para fazer novas classes ordenadas.
import enum
from functools import total_ordering


@total_ordering
@enum.unique
class order(enum.Enum):
    one = 1
    two = 2
    three = 3
    four = 4

    def __lt__(self, other):
        return isinstance(other, order) and self.value < other.value

    def __eq__(self, other):
        if isinstance(other, order):
            return self.value == other.value
        elif isinstance(other, int):
            return  self.value == other
        elif isinstance(other, float):
            return self.value == other
        else:
            return False


print(order.one.name)
print(order.one.value)
print(order.four > order.two)
print(order.four == order.three)
print(order.four >= order.one)

