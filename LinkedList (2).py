class LinkedList:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

LL = LinkedList(10)
LL.next = LinkedList(20)
LL.next.next = LinkedList(100)

LL1 = LinkedList(10)
LL1.next = LinkedList(20)
LL1.next.next = LinkedList(100)

def merge2(LL,LL1):
    dummy = LinkedList()
    tail = dummy
    temp = LL
    temp1 = LL1
    while(temp and temp1):
        if(temp.data <= temp1.data):
            tail.next = temp
            temp=temp.next
        elif(temp.data >= temp1.data):
            tail.next = temp1
            temp1=temp1.next
        tail = tail.next
    return dummy.next
    

def display(LL):
    temp = LL
    while(temp):
        print(temp.data)
        temp = temp.next

#display(LL)
#display(LL1)
LL2 = merge2(LL,LL1)
display(LL2)

