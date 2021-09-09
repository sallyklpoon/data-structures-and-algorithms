"""
Uses heapq

Code adapted from Robin Andrews
"""
import heapq


class PriorityQueue:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]  # heapq.heappop returns tuple, we only want value, not the priority num

    def __str__(self):
        return str(self.elements)


if __name__ == '__main__':
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())
    pq.put("eat", 2)
    pq.put("coding", 1)
    pq.put("sleep", 3)
    print(pq)
