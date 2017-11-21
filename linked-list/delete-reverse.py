class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def list(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next

    def delete(self):
        prev = None
        node = self.head
        self.head = None
        while(node):
            prev = node
            node = node.next
            prev.next = None
            prev = None

    def reverse(self):
        prev = self.head
        current = self.head.next
        self.head.next = None
        self.head = None

        while(current):
            nextN = current.next
            current.next = prev
            prev = current
            current = nextN

        self.head = prev


l = LinkedList()
l.head = Node(1)
l.head.next = Node(2)
l.head.next.next = Node(3)
l.head.next.next.next = Node(4)
l.reverse()
l.list()
