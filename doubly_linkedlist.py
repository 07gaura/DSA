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
            
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not Empty")
            
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head.pref = new_node
            self.head = new_node
            
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            new_node.pref = n
            
            
    def delete_end(self):
        n = self.head
        while n.nref.nref is not None:
            n = n.nref
        n.nref = None
        
dll = doublyll()
dll.add_begin(10)
dll.add_begin(20)
dll.add_begin(10)
dll.delete_end()
dll.print_ll()
         
