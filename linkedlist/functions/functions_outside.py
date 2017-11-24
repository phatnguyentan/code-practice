from ..node import *
# outside class functions

# Merge 2 List
# @params head1
# @params head2
def mergeList(head1, head2):
    s = t = Node(1)
    while 1:
        # if head is None, t -> others head
        if head1 is None:
            t.next = head2
            break
        if head2 is None:
            t.next = head1
            break
        # c = min head data, then head = head.next
        if head1.data < head2.data:
            c = head1
            head1 = head1.next
        else:
            c = head2
            head2 = head2.next
        # t -> c
        t.next = c
        t = t.next
    # return source
    return s.next
