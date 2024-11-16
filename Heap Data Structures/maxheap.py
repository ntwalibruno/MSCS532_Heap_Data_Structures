class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)].Priority < self.heap[index].Priority:
            parent_index = self.parent(index)
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left].Priority > self.heap[largest].Priority:
            largest = left
        
        if right < len(self.heap) and self.heap[right].Priority > self.heap[largest].Priority:
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            raise IndexError("Extract from an empty heap")
        
        max_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return max_element

    def peek(self):
        if not self.heap:
            raise IndexError("Peek from an empty heap")
        return self.heap[0]

    def size(self):
        return len(self.heap)