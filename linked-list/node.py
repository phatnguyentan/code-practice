class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

l = LinkedList()
l.head = Node(1)
l.head.next = Node(2)
print(l.head.next.data)
