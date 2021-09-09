"""
Python Data Structures
queue_ds class using List

Not the best because de-queueing will take time as the indexes of the list must be re-adjusted
"""


class QueueList:

    def __init__(self):
        """
        Instantiate a queue_ds class object.
        """
        self.items = []

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

    def enqueue(self, item):
        """
        Add passed item to queue_ds.

        :param item: any data structure
        :postcondition: add passed item to queue_ds
        :return: none
        """
        self.items.append(item)

    def dequeue(self):
        """
        Dequeue by returning the first item from the queue_ds.

        :postcondition: remove the item at the front of the queue_ds
        :return: the item at the head of the queue_ds
        """
        self.items.pop(0)

    def __str__(self):
        """
        Return queue_ds's items if printed.

        :return: a String, the items in queue_ds
        """
        return str(self.items)
