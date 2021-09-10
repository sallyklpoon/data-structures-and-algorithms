"""
Implementation of a single linked list node.
"""


class SllNode:

    def __init__(self, data):
        """
        Instantiate a Node class.

        Done in constant time.

        :param data: any data type
        :postcondition: instantiate a Node object
        """
        self.data = data
        self.next = None

    def __repr__(self):
        """
        Return printable representation of the node.

        :return: String
        """
        return f"SLLNode object: data={self.data}"

    def get_data(self):
        """
        Return the data of the node.

        Done in constant time

        :return: the data of the node
        """
        return self.data

    def set_data(self, new_data):
        """
        Update the node's data.

        Done in constant time

        :param new_data: a new data type to override current data
        :return: None, the node's data is updated
        """
        self.data = new_data

    def get_next(self):
        """
        Return the next node attribute.

        :return: the next node object
        """
        return self.next

    def set_next(self, new_next):
        """
        Replace the existing value of the self.next attribute with new_next

        :param new_next: a Node object
        :return: None, the current node with self.next updated
        """
        self.next = new_next

    def is_last(self):
        """
        Return True if node is at the end of the SLL, False if it is not the last element in the SLL.

        :return: Boolean. True if node is at end of SLL, else, False
        """
        return self.next is None
