class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insertH(self, node):
        node.next = self.head
        self.head = node

    def list(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next

    def swap(self, dataX, dataY):
        prev = None
        prevX = None
        prevY = None
        x = None
        y = None
        tmp = self.head
        while(tmp):
            if(tmp.data == dataX):
                x = tmp
                prevX = prev
            if(tmp.data == dataY):
                y = tmp
                prevY = prev
            prev = tmp
            tmp = tmp.next
        if prevX != None:
            prevX.next = y
        else:
            self.head = y
        if prevY != None:
            prevY.next = x
        else:
            self.head = x

        nextX = x.next
        x.next = y.next
        y.next = nextX

l = LinkedList()
l.insertH(Node(4))
l.insertH(Node(3))
l.insertH(Node(2))
l.insertH(Node(1))
l.list()
l.swap(2, 3)
l.list()
