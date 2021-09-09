"""
Python Data Structures - Queue
Queue class using deque data structure built-in to Python library
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the head of the queue.

        :postcondition: return the item at the head of the queue and remove it
        :return: the item at the head of the queue
        """
        return self.items.popleft()
