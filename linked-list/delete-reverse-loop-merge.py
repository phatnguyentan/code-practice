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

    def isLoop(self):
        node = self.head.next
        prev = self.head
        while(node):
            if node.data <= prev.data:
                return True
            prev = node
            node = node.next
        return False

l = LinkedList()
l.head = Node(1)
l.head.next = Node(2)
l.head.next.next = Node(3)
l.head.next.next.next = Node(4)
# l.head.next.next.next.next = l.head.next
# l.reverse()
print(l.isLoop())
# l.list()
