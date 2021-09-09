"""
Python Data Structures
queue class using List

Not the best because de-queueing will take time as the indexes of the list must be re-adjusted
"""


class QueueList:

    def __init__(self):
        """
        Instantiate a queue class object.
        """
        self.items = []

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

    def enqueue(self, item):
        """
        Add passed item to queue.

        :param item: any data structure
        :postcondition: add passed item to queue
        :return: none
        """
        self.items.append(item)

    def dequeue(self):
        """
        Dequeue by returning the first item from the queue.

        :postcondition: remove the item at the front of the queue
        :return: the item at the head of the queue
        """
        self.items.pop(0)

    def __str__(self):
        """
        Return queue's items if printed.

        :return: a String, the items in queue
        """
        return str(self.items)
