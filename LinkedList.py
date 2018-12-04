"""
LinkedList that supports delete value,
prepend, append, and print

2016

"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):

        if not self.head:
            self.head = Node(value)
            return

        q = self.head

        while q.next:
            q = q.next
        q.next = Node(value)
        return self.head

    def prepend(self, value):

        if not self.head:
            self.head = Node(value)
            return

        toAdd = Node(value)
        toAdd.next = self.head
        self.head = toAdd

    def deleteValue(self, value):

        if not self.head:
            return False

        if self.head.value == value:
            self.head = self.head.next
            return True

        q = self.head
        while q.next:
            if q.next.value == value:
                q.next = q.next.next
                return True
            q = q.next
        return False

    def print(self):
        q = self.head
        while q:
            print(q.value)
            q = q.next









