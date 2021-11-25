queue = []
def enqueue():
    print("Enter the no")
    num = int(input())
    queue.append(num)
    
def size():
    return len(queue)
    
def dequeue():
    if(size()==0):
        print("queue is Empty")
    else:
        queue.pop(0)
        print("Element is popped successfully")
        
def printQueue():
    for i in queue:
        print(i)
        
def main():
    while True:
        print("Enter the no 1) Enqueue  2) Dequeue 3) Size 4) print 5) Exit")
        no = int(input())
        if(no == 1):
            enqueue()
        elif(no == 2):
            dequeue()
        elif(no == 3):
            print("size of queue is", size())
        elif(no == 4):
            printQueue()
        elif(no == 5):
            break
        else:
            print("please select a valid input")

if __name__ == "__main__":
    main()
