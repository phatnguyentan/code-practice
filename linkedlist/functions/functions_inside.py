# inside class functions
def insertHead(self, node):
    node.next = self.head
    self.head = node

def insertTail(self, node):
    if self.head is None:
        self.head = node
        return
    n = self.head
    while(n.next is not None):
        n = n.next
    n.next = node

def list(self):
    if self.isLoop():
        self.loopAt()
        return
    arr = []
    n = self.head
    while(n):
        arr.append(str(n.data))
        n = n.next
    print(" -> ".join(arr))

def listFull(self):
    arr = []
    n = self.head
    while(n):
        arr.append(str(n.data) + ":" + str(n))
        n = n.next
    print(" -> ".join(arr))


def isLoop(self):
    v = {}
    n = self.head
    while n:
        if v.get(n.data) == True:
            return True
        v[n.data] = True
        n = n.next
    return False

def loopAt(self):
    v = {}
    n = self.head
    arr = [str(self.head.data)]
    while n:
        if v.get(n.data) == True:
            print("Loop: ", " -> ".join(arr))
            return n
        v[n.data] = True
        n = n.next
        arr.append(str(n.data))
