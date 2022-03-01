class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height=None

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

def levelOrder(root):
    if root is None:
        return 
    queue=[]
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].data)
        n = queue.pop(0)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
    
def leftView(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    while(len(queue)>0):
        n=len(queue)
        for i in range(1,n+1):
            temp = queue[0]
            queue.pop(0)
            if(i==1):
                print(temp.val)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
    
def rightView(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    while(len(queue)>0):
        n=len(queue)
        for i in range(1,n+1):
            temp = queue[0]
            queue.pop(0)
            if(i==2):
                print(temp.val)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
                
def levelOrderSpiral(root):
    if root is None:
        return
    s1=[]
    s2=[]
    count=1
    s1.append(root)
    while(len(s1)>0 or len(s2)>0):
        n1=len(s1)
        print("level ",count)
        for i in range(0,n1):
            temp=s1.pop(0)
            print(temp.val)
            if temp.left is not None:
                s2.append(temp.left)
            if temp.right is not None:
                s2.append(temp.right)
        n2=len(s2)
        for i in range(0,n2):
            temp=s2.pop(0)
            print(temp.val)
            if temp.left is not None:
                s1.append(temp.left)
            if temp.right is not None:
                s1.append(temp.right)
        count+=1
        
def givenLevelOrderSpiral(root,index1,index2):
    if root is None:
        return
    s1=[]
    s2=[]
    count=1
    s1.append(root)
    while(len(s1)>0 or len(s2)>0):
        n1=len(s1)
        for i in range(0,n1):
            temp=s1.pop(0)
            if index1<=count and index2>=count:
                print(temp.val)
            if temp.left is not None:
                s2.append(temp.left)
            if temp.right is not None:
                s2.append(temp.right)
        n2=len(s2)
        for i in range(0,n2):
            if index1<=count and index2>=count:
                temp=s2.pop(0)
            print(temp.val)
            if temp.left is not None:
                s1.append(temp.left)
            if temp.right is not None:
                s1.append(temp.right)
        count+=1
    
def TopView(root):
    if root is None:
        return
    queue=[]
    mydicts=dict()
    hd=0
    root.height = hd
    queue.append(root)
    
    while len(queue):
        temp = queue.pop(0)
        hd = temp.height
        
        if hd not in mydicts:
            mydicts[hd] = temp.val
        
        if temp.left is not None:
            temp.left.height = hd-1
            queue.append(temp.left)
        if temp.right is not None:
            temp.right.height = hd+1
            queue.append(temp.right)
            
    print(mydicts)
    
def BottomView(root):
    if root is None:
        return
    queue=[]
    mydicts=dict()
    hd=0
    root.height = hd
    queue.append(root)
    
    while len(queue):
        temp = queue.pop(0)
        hd = temp.height
        
        mydicts[hd] = temp.val
        
        if temp.left is not None:
            temp.left.height = hd-1
            queue.append(temp.left)
        if temp.right is not None:
            temp.right.height = hd+1
            queue.append(temp.right)
            
    print(mydicts)
    
def maxWidth(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    maxs=0
    count=1
    while len(queue):
        count=len(queue)
        maxs = max(maxs,count)
        while count!=0:
            temp = queue.pop()
            count-=1
            if temp.left is not None:
                queue.insert(0,temp.left)
            if temp.right is not None:
                queue.insert(0,temp.right)
    print(maxs)
    
def buildTree(root):
    if root is None:
        return
    nodes = []
    ittrNodes(root,nodes)
    return buildBalanceTree(nodes,0,len(nodes)-1)
    
def ittrNodes(root,nodes):
    if root is None:
        return 
    ittrNodes(root.left,nodes)
    nodes.append(root)
    ittrNodes(root.right,nodes)
    
def buildBalanceTree(nodes,start,end):
    if start>end:
        return None
    mid = (end + start)//2
    node = nodes[mid]
    #print(node.val)
    node.left=buildBalanceTree(nodes,start,mid-1)
    node.right=buildBalanceTree(nodes,mid+1,end)
    return node
    
root = None
root = insert(root, 10)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 8)
root = insert(root, 15)
root = insert(root, 12)
root = insert(root, 14)

root = buildTree(root)
inOrder(root)
