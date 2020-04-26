# Simple MaxHeap implementation

class Heap(object):

    def __init__(self, items = []):
        self.items = [0]
        for item in items:
            self.items.append(item)
            self.__bubbleup(len(self.items) - 1)
    
    def push(self, item):
        self.items.append(item)
        self.__bubbleup(len(self.items) - 1)
    
    def peek(self):
        if len(self.items) >= 2:
            return self.items[1]
        else:
            return None

    def pop(self):
        if len(self.items) >= 2:
            self.__swap(1, len(self.items) - 1)
            max_item = self.items.pop()
            self.__bubbledown(1)
            return max_item
        return None
    

    def __swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
    

    def __bubbleup(self, index):
        parent = index // 2
        if index <= 1:
            return
        if self.items[index] > self.items[parent]:
            self.__swap(parent, index)
            self.__bubbleup(parent)
    
    def __bubbledown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.items) > left and self.items[left] > self.items[largest]:
            largest = left
        if len(self.items) > right and self.items[right] > self.items[largest]:
            largest = right
        if largest != index:
            self.__swap(largest, index)
            self.__bubbledown(largest)

heap = Heap([2, 50, 100, 1])
heap.push(1000)
heap.push(-1000)
print(heap.peek() == 1000)

        