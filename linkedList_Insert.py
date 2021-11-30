class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_ll(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
                
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def length(self):
        n = self.head
        count=0
        while n is not None:
            n = n.ref
            count+=1
        return count
        
    def add_position(self, data, pos):
        new_node = Node(data)
        count = 1
        if self.head is None:
            self.head = new_node
        elif pos == 1:
            new_node.ref = self.head
            self.head = new_node
        elif self.length()>=pos:
            n = self.head
            while n is not None:
                if count == pos-1:
                    break
                n = n.ref
                count +=1
            new_node.ref = n.ref
            n.ref = new_node
        else:
            print("Wrong position")
        
        def add_after(self, data,x):
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.ref
            if n is None:
                print("Node is not present in list")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
                
ll1 = LinkedList()
ll1.add_begin(20)
ll1.add_end(10)
ll1.add_position(30,2)
ll1.print_ll()
