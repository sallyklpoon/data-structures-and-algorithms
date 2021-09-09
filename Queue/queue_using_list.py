"""
Python Data Structures
Queue class using List

Not the best because de-queueing will take time as the indexes of the list must be re-adjusted
"""


class QueueList:

    def __init__(self):
        """
        Instantiate a Queue class object.
        """
        self.items = []

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
        return str(self.items)
