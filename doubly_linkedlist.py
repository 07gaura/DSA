class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
        
class doublyll:
    def __init__(self):
        self.head = None
        
    def print_ll(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n=n.nref
                
    def print_llreverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data)
                n = n.pref
            
            
