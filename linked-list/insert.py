class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, node):
        node.next = self.head
        self.head = node
        return node

    def insertTail(self, node):
        n = self.head
        while(n.next):
            n = n.next
        n.next = node
        return node

    def insertHeadAfter(self, number, node):
        p = self.head
        if(number == 0):
            self.insertHead(node)
        number -= 1
        while(p and number > 0):
            number -= 1
            p = p.next
        if(number == 0):
            node.next = p.next
            p.next = node
        return node

    def deleteKey(self, key):
        tmp = self.head
        prev = None
        while(tmp):
            if(tmp.data == key):
                if(prev != None):
                    self.deleteNode(prev)
                else:
                    self.deleteNode()
                return
            else:
                prev = tmp
                tmp = tmp.next

    def deleteNode(self, prev = None):
        if(prev == None):
            tmp = self.head
            self.head = self.head.next
            tmp = None
            return
        tmp = prev.next
        prev.next = prev.next.next
        tmp = None

    def length(self):
        tmp = self.head
        number = 0
        while (tmp):
            number += 1
            tmp = tmp.next
        return number

    def search(self, x):
        tmp = self.head
        while(tmp):
            if(tmp.data == x):
                return tmp
            tmp = tmp.next
        return None

    def list(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next

l = LinkedList()
n1 = l.insertHead(Node(1))
n2 = l.insertTail(Node(2))
n3 = l.insertTail(Node(3))
n4 = l.insertHeadAfter(3, Node(4))
n5 = l.insertTail(Node(5))
n6 = l.insertTail(Node(6))

l.list()
