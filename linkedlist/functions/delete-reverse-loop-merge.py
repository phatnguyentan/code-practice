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

    def move(self, src, new):
        # new = src
        # src = new.next
        # new.next = des
        # des = new
        src.next = new
        new.next = src

def merge_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    s = t = Node()
    while not (head1 is None or head2 is None):
        if head1.data < head2.data:
            c = head1
            head1 = head1.next
        else:
            c = head2
            head2 = head2.next

        t.next = c
        t = t.next

    t.next = head1 or head2
    return s.next

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
head = merge_lists(l.head, l2.head)
l3 = LinkedList()
l3.head = head
l3.list()

# l.head.next.next.next.next = l.head.next
# l.reverse()
# print(l.isLoop())
# l.list()
