"""
Queue that supports enqueue, dequeue, print,
empty, size

2016
"""


class Queue:

    def __init__(self):
        self.items = []

    def dequeue(self):
        return self.items.pop()

    def enqueue(self, value):
        self.items.append(value)

    def print_queue(self):

        for item in self.items:
            print(item)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
