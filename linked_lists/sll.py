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
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def size(self):
        """
        Return the size of the SLL.

        Time complexity is O(n) because every Node in the Linked List must be visited.

        :return: an integer, the size of the SLL
        """
        current_node = self.head
        size = 0
        if current_node is None:
            return size
        while current_node is not None:
            size += 1
            current_node = current_node.get_next()
        return size

    def search(self, data):
        """
        Return true if data searched is found in the SLL, else, return False.

        :param data: a data type
        :return: Boolean, True if the data indicated is found in linked list, else, False
        """
        if self.head is None:
            return "Linked List is empty."
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.get_next()
        return False

    def remove(self, data):
        """
        Remove the first instance of a node containing passed data parameter from Linked List.

        Time complexity O(n) because worst case is to reach n max Linked List length.

        :param data: a data type
        :return: None, removes a node
        """
        if self.head is None:
            return "Linked List is empty."
        elif self.search(data) is False:
            return "Data not found in Linked List."
        elif self.head.get_data() == data:
            self.head = self.head.get_next()
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.next.data == data:
                    remove_node = current_node.get_next()
                    current_node.set_next(remove_node.get_next())
                    return
                current_node = current_node.get_next()


if __name__ == '__main__':
    my_sll = Sll()
    print(my_sll.remove(14))
    my_sll.add_front(33)
    my_sll.remove(33)
    print(my_sll.is_empty())
    my_sll.add_rear(1)
    my_sll.remove(1)
    print(my_sll.is_empty())
    my_sll.add_rear(1)
    my_sll.add_rear(2)
    my_sll.add_rear(3)
    print(my_sll.size())
    my_sll.remove(2)
    print(my_sll.size())
    print(my_sll.search(2))
    print(my_sll.remove(5))
    my_sll.remove(3)
    print(my_sll.size())
    print(my_sll.search(3))
