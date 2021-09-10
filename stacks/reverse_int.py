"""
REVERSE INTEGER

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def add(self, item):
        self.items.append(item)


def reverse(integer: int) -> int:
    """
    Reverse the digits of an integer, keeping the correct sign. If number goes out of 32-bit range, return 0.
    
    :param integer: an Integer
    :return: an integer, the accepted integer parameter reversed
    """
    original_num = Stack()
    new_num_stack = Stack()
    sign = False
    if integer < 0:
        sign = True
        integer = integer * -1
    original_num.items = [num_str for num_str in str(integer)]
    while not original_num.is_empty():
        new_num_stack.add(original_num.pop())
    new_num_int = int("".join(new_num_stack.items))

    if sign:
        return new_num_int * -1
    elif new_num_int not in range(-231, 230):
        return 0
    return new_num_int


if __name__ == '__main__':
    print(reverse(-123))
