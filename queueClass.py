class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
    
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        
    def addQ(self,d):
        new_node = Node(d)
        if self.head is None:
            self.head = new_node
        else:
            self.last.ref = new_node
        self.last = new_node
            
    def dequeu(self):
        if self.head is None:
            return "Queue is empty"
        else:
            self.head = self.head.ref 
        if self.head is None:
            self.last = None
            
    def printq(self):
        if self.head is None:
            return "Queue is empty"
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
                
ql = Queue()
ql.addQ(10)
ql.addQ(20)
ql.addQ(20)
ql.addQ(20)
ql.printq()
