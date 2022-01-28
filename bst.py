class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,data):
    if root is None:
        return Node(data)
    else:
        if root.val == data:
            return root
        elif root.val<data:
            root.right = insert(root.right,data)
        elif root.val>data:
            root.left = insert(root.left,data)
    return root

def inOrder(root):
    if root is None:
        return 
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)
    
def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)
        
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
# Print inoder traversal of the BST
inOrder(r)
