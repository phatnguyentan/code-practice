class Node:
    def __init__(self, data = None):
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

    def merge(self, list):
        node1 = self.head
        node2 = list.head
        l = LinkedList()
        l.head = Node()

        while node1 and node2:
            if node1.data > node2.data:
                n = node2.next
                self.move(node2, l.head)
                node2 = n
            else:
                n = node1.next
                self.move(node1, l.head)
                node1 = n

        return l

    def move(self, src, new):
        # new = src
        # src = new.next
        # new.next = des
        # des = new
        src.next = new
        new.next = src

l = LinkedList()
l.head = Node(1)
l.head.next = Node(3)
l.head.next.next = Node(4)
l.head.next.next.next = Node(6)
l2 = LinkedList()
l2.head = Node(2)
l2.head.next = Node(4)
l2.head.next.next = Node(5)
l2.head.next.next.next = Node(7)
l3 = l.merge(l2)
print(l3.head.data)
print(l3.head.next.data)
print(l3.head.next.next.data)
# l.head.next.next.next.next = l.head.next
# l.reverse()
# print(l.isLoop())
# l.list()
