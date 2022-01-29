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

def delete(root,data):
    if root is None:
        return root
    elif root.val<data:
        root.right = delete(root.right,data)
    elif root.val>data:
        root.left = delete(root.left,data)
    else:
        if root.left is None and root.right is None:
            return None
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = getSuccessor(root)
        root.val=temp.val
        root.right = delete(root.right,temp.val)
    return root
        
def getSuccessor(root):
    if root is None:
        return None
    temp = root.right
    while temp.left is not None:
        temp = temp.left
    return temp
    
        
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
root = delete(root, 20)
root = delete(root, 50)
# Print inoder traversal of the BST
inOrder(root)
