def push(count):
    if(count==n):
        print("Stack Overflow")
        return count
    else:
        num=int(input("Enter the element to insert: "))
        a.append(num)
        print(a[count],"is inserted")
        count+=1
        print("count:", count)
        return count
def pop(count):
    if(count==0):
        print("Stack Underflow")
        return count
    else:
        count-=1
        print("Deleted element is", a[count])
        a.pop()
        return count
def disp():
    if(len(a)==0):
        print("Stack Underflow")
    else:
        print("The stack is", a)
def peek():
    if(len(a)==0):
        print("Stack Underflow")
    else:
        print("The top element of the stack is", a[len(a) - 1])
print("Stack using array list")
n=int(input("Enter the limit: "))
a=[]
c=0
while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Peek\n5. Exit")
    o=int(input("Enter your choice: "))
    if(o==1):
        c=push(c)
    elif(o==2):
        c=pop(c)
    elif(o==3):
        disp()
    elif(o==4):
        peek()
    elif(o==5):
        print("Thank You")
        break
    else:
        print("Wrong Choice")