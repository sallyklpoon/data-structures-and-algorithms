"""
Modification of Erin Allard's course code 'Python Data Structures: Stacks, Queues, and Dequeues'
"""


class Stack:

    def __init__(self):
        """Instantiate Stack() object
        """
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

        :return: the top item of the stack if Stack is not empty
        """
        try:
            return self.items.pop()  # pop without any param will always return item at index -1
        except IndexError:
            print("Oops! Your stack is empty, there is nothing to remove.")

    def peek(self):
        """Return the next item that can be removed (top of the stack) if the stack is non-empty.
        The run-time for this method is O(1), as indexing is at constant time.

        :return: the last/top-most item in the stack if the stack is non-empty
        """
        try:
            return self.items[-1]
        except IndexError:
            print("There is nothing in your stack.")

    def size(self) -> int:
        """Return how many items are in the stack.
        This method runs in O(1) because finding length of list happens in constant time.

        :return: an integer, the size/length of the stack
        """
        return len(self.items)

    def is_empty(self) -> bool:
        """Return true if Stack is empty, false if it is non-empty.
        This method runs O(1), testing in equality happens in constant time.

        :return: boolean, True if stack is empty, false if it is non-empty
        """
        return self.items == []

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    
