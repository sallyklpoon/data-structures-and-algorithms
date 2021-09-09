"""
Python Data Structures - queue_ds
queue_ds class using deque data structure built-in to Python library
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self) -> bool:
        """
        Indicate if the queue_ds is empty.

        :return: a boolean, true if queue_ds is empty, false if the queue_ds is not empty
        """
        return not self.items

    def size(self) -> int:
        """
        Give the size of the queue_ds.

        :return: an integer, the size of the queue_ds
        """
        return len(self.items)

    def peek(self):
        """
        Return the item at the head of the queue_ds without deletion.

        :return: item at the head of the queue_ds
        """
        return self.items[0]

    def enqueue(self, item) -> None:
        """
        Add item to queue_ds.

        :param item: an item
        :postcondition: queue_ds has item added to the end of it
        :return: nothing
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the head of the queue_ds.

        :postcondition: return the item at the head of the queue_ds and remove it
        :return: the item at the head of the queue_ds
        """
        return self.items.popleft()

    def __str__(self):
        """
        Return queue_ds's items if printed.

        :return: a String, the items in queue_ds
        """
        return str(self.items)
