"""
Given a string of bracket symbols, determine if the string is balanced.
"""

import stack


def balanced_brackets(brackets: str) -> bool:
    """Return boolean if a given string of brackets is balanced.

    :param brackets: a String
    :precondition: String contains bracket characters only: "(){}[]"
    :postcondition: return true if bracket string is balanced, return false if bracket string is not balanced
    :return: Boolean
    """
    open_brackets = "[{("
    bracket_pair = {"]": "[", "}": "{", ")": "("}
    given_brackets, evaluate_stack = stack.Stack(), stack.Stack()
    given_brackets.items = list(brackets)
    while not given_brackets.is_empty():
        if given_brackets.peek() not in open_brackets:
            evaluate_stack.add(given_brackets.remove())
        elif given_brackets.peek() == bracket_pair[evaluate_stack.peek()]:
            given_brackets.remove()
            evaluate_stack.remove()
        else:
            break
    return len(evaluate_stack.items) == 0


if __name__ == '__main__':
    print(balanced_brackets("({}{{}})"))
