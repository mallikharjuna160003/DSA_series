class DLinkedList:
    def __init__(self,value=None,next=None,prev=None):
        self.val = value
        self.prev = prev
        self.next = next

class MiddleStack:
    
    def __init__(self):
        self.head = DLinkedList()
        self.dummy = DLinkedList()
        self.mid = self.dummy
        self.cnt = 0
        
    def push(self,x):
        curr = DLinkedList(value=x,next=None,prev=None)
        curr.next = self.head
        self.head.prev = curr
        self.head = curr
        self.cnt+=1
        if self.cnt==1:
            self.mid = curr
        elif self.cnt%2 == 0:
            self.mid = self.mid.prev
    def pop(self):
        if(self.cnt==0):
            return -1
        x = self.head.val
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None
        self.cnt-=1
        if self.cnt&1:
            self.mid = self.mid.next
        return x
    
    def middle(self):
        if(self.cnt ==0):
            return -1
        print("middle",self.mid.val)
    def display(self):
        temp = self.head
        for i in range(self.cnt):
            print(temp.val,end=" ")
            temp = temp.next

obj = MiddleStack()
obj.push(10)
obj.push(20)
obj.push(30)
#obj.push(40)
obj.middle()
obj.display()
    
    
