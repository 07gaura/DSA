import collections
queue = collections.deque()

def append():
    print("Enter the no")
    num = int(input())
    queue.appendleft(num)

def size():
    print(len(queue))
    
def delete():
    if not queue:
        print("no elements left")
    else:
        queue.pop()
    
def printqueue():
    for i in queue:
        print(i)
def main():
    while True: 
        print("Select the options 1) append 2) delete 3) size 4) print all elements 5) exit")
        no = int(input())
        if (no == 1):
            append()
        elif (no == 2):
            delete()
        elif (no == 3):
            size()
        elif (no == 4):
            printqueue()
        elif (no == 5):
            break
        else:
            print("Please Enter the Correct input")
            
if __name__ == "__main__":
    main()
