queue = []
def append():
    print("Enter the No")
    num = int(input())
    queue.append(num)
    
def sort():
    for i in range(0, len(queue)):
        for j in range(0, len(queue)):
            if(queue[i]<queue[j]):
                temp = queue[i]
                queue[i] = queue[j]
                queue[j] = temp
def size():
    return len(queue)
    
def delete():
    if(size()==0):
        print("All elements are deleted")
    else:
        sort()
        res = queue.pop()
        print(res)
        
def printqueue():
    for i in queue:
        print(i)
        
def main():
    while True:
        print("select the options 1. Append 2. Delete 3. size 4. print 5. Exit ")
        no = int(input())
        if(no == 1):
            append()
        elif(no == 2):
            delete()
        elif(no == 3):
            size()
        elif(no == 4):
            printqueue()
        elif(no == 5):
            break
        else:
            print("Enter the correct input")
            
if __name__ == "__main__":
    main()
