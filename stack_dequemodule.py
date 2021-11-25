import collections

stack = collections.deque()

def add():
    print("Enter the no")
    no = int(input())
    stack.append(no)
    
def remove():
    if(size()==0):
        print("No elements are present")
    else:
        stack.pop()
def size():
    return len(stack)
    
def printstack():
    for i in stack:
        print(i)

def topstack():
    print(stack[-1])

def main():
    while True:
        print("Select any options 1: Add 2: Remove 3: Size 4: print 5: Top 6: exit")
        no = int(input())
        if(no == 1):
            add()
        elif(no == 2):
            remove()
        elif( no == 3):
            print(size())
        elif( no == 4):
            printstack()
        elif( no == 5):
            topstack()
        elif( no == 6):
            break
        else:
            print("Enter the correct input")
if __name__ == "__main__":
    main()
