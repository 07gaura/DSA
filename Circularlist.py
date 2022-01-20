class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
    
class circularList:
    def __init__(self):
        self.last =None
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            
        else:
            new_node.ref = self.last.ref
        self.last.ref = new_node
        
    def add_last(self,data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.last.ref = new_node
        else:
            temp = self.last.ref
            self.last.ref = new_node
            new_node.ref = temp
        
    def printCL(self):
        if self.last is None:
            return "List is empty"
        else:
            n = self.last.ref
            while n is not self.last:
                print(n.data)
                n = n.ref
            print(n.data)
    
    def delete_first(self):
        
        if self.last is None:
            return "List is empty"
        elif self.last.ref == self.last:
            self.last = None
            return
        else:
            n = self.last.ref
            self.last.ref = self.last.ref.ref
            n.ref = None
            
cl = circularList()
cl.add_last(40)

print(cl.delete_first())
cl.printCL()
