"""
Stack that supports push, pop, size, empty,
and print

2016

"""


class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def print_stack(self):

        for item in self.items:
            print(item)
