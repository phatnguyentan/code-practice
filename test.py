from linkedlist.linkedlist import *

l = LinkedList()
l.insertTail(Node(1))
l.insertTail(Node(2))
l.insertTail(Node(3))
l.head.next.next = l.head
l.list()

# l2 = LinkedList()
# l2.insertTail(Node(1))
# l2.insertTail(Node(4))
# l2.insertTail(Node(6))
#
# l3 = LinkedList()
# l3.head = mergeList(l.head, l2.head)
