from maxheap import MaxHeap;
class PriorityQueue:
    def __init__(self):
        self.max_heap = MaxHeap()

    def insert(self, element):
        self.max_heap.insert(element)

    def extract_max(self):
        return self.max_heap.extract_max()

    def peek(self):
        return self.max_heap.peek()

    def size(self):
        return self.max_heap.size()
