"""
Python Data Structures - queue
queue class using deque data structure built-in to Python library
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self) -> bool:
        """
        Indicate if the queue is empty.

        :return: a boolean, true if queue is empty, false if the queue is not empty
        """
        return not self.items

    def size(self) -> int:
        """
        Give the size of the queue.

        :return: an integer, the size of the queue
        """
        return len(self.items)

    def peek(self):
        """
        Return the item at the head of the queue without deletion.

        :return: item at the head of the queue
        """
        return self.items[0]

    def enqueue(self, item) -> None:
        """
        Add item to queue.

        :param item: an item
        :postcondition: queue has item added to the end of it
        :return: nothing
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the head of the queue.

        :postcondition: return the item at the head of the queue and remove it
        :return: the item at the head of the queue
        """
        return self.items.popleft()

    def __str__(self):
        """
        Return queue's items if printed.

        :return: a String, the items in queue
        """
        return str(self.items)
