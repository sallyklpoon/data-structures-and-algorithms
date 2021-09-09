
import stack


def reverse_string(message: str) -> str:
    """Reverse the order of a message using a stack.

    :param message: a String
    :precondition: input is a string
    :postcondition: return the message characters reversed in order
    :return: a String
    """
    original_stack = stack.Stack()
    original_stack.items = [character for character in message]
    output = ""
    while not original_stack.is_empty():
        output += original_stack.pop()
    return output


if __name__ == '__main__':
    my_string = "!dLroW 0lL3h"
    print(reverse_string(my_string))
