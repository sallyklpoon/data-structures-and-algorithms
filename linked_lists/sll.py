"""
Implement single linked-list class.
"""
from sll_node import SllNode

class Sll:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"SLL object: head={self.head}"

    def is_empty(self):
        """
        Return true if SLL is empty, else, false.

        Complete in constant time

        :return: Boolean, true if SLL is empty, else false
        """
        return self.head is None

    def add_front(self, new_data):
        """
        Add a new node to the front of the SLL using new_data

        :param new_data: any data type
        :return: None, a new node added to the front of the linked list
        """
        new_node = SllNode(new_data)
        new_node.set_next(self.head)
        self.head = new_node

    def add_rear(self, new_data):
        """
        Add a new node at the end of an SLL.

        :param new_data: a data type
        :return: None, a new node added to the end of the SLL
        """
        new_node = SllNode(new_data)
        current_node = self.head
        if current_node is None:
            self.head = new_node
            return
        while current_node.next is not None:
            current_node = current_node.next
        current_node.set_next(new_node)

    def size(self):
        pass

    def search(self, data):
        pass

    def remove(self, data):
        pass


if __name__ == '__main__':
    my_sll = Sll()
    node1 = SllNode(1)
    node2 = SllNode(2)
    node3 = SllNode(3)
    my_sll.add_rear(node1)
    print(my_sll)
    my_sll.add_rear(node2)
    print(my_sll)
    print(my_sll.head.next)
