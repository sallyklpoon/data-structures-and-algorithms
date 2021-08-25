class Stack:

    def __init__(self):
        self.items = []

    def add(self, item) -> None:
        """Accept an item and append it to the end of the stack.
        The run-time for this method is O(1), or constant time, because appending to the end of a list happens
        at constant time.

        :param item: a data type that can be accepted to a list
        :return: None
        """
        self.items.append(item)

    def remove(self):
        """Remove and return the top item from the stack.
        The run-time for this method is O(1), as indexing is at constant time.

        :return: the top item of the stack
        """
        try:
            return self.items.pop()  # pop without any param will always return item at index -1
        except IndexError:
            print('Oops! Your stack is empty, there is nothing to remove.')

    def peek(self):
        """Return the next item that can be removed (top of the stack)."""
        return self.items[-1]

    def size(self):
        """Return how many items are in the stack."""
        return len(self.items)

    def is_empty(self) -> bool:
        """Determine if the stack is empty."""
        return self.items == []
