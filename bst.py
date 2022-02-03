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
    
def getSum(root):
    if root is None:
        return 0
    return root.val + getSum(root.right)+getSum(root.left)

def getLeafNodeCount(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return getLeafNodeCount(root.left)+getLeafNodeCount(root.right)
    
def getNodeCount(root):
    if root is None:
        return 0
    return getNodeCount(root.left)+getNodeCount(root.right)
    
def heightOfTree(root):
    if root is None:
        return -1
    no=heightOfTree(root.left)
    no1=heightOfTree(root.right)
    if no>no1:
        return no+1
    else:
        return no1+1

def leveOrderTraversal(root):
    if root is None:
        return
    hieght = heightOfTree(root)
    for i in range(0,hieght+1):
        Traverse(root,i+1)
        print("-----")
    
def Traverse(root,h):
    if root is None:
        return
    if h==1:
        print(root.val)
        return
    Traverse(root.left,h-1)
    Traverse(root.right,h-1)
    
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Print inoder traversal of the BST

leveOrderTraversal(root)
