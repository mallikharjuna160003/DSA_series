class TwoStackArray:
    
    def __init__(self):
        self.arr = [-1]*6
        self.t1 = -1
        self.t2 = 6
        self.size = 6
        
        
    def push1(self,x):
        if self.t1 <self.t2 and self.arr[self.t2-1]==-1:
            self.t1+=1
            self.arr[self.t1]=x
        else:
            print("Already elements of st2 present")
            
    def push2(self,x):
        if self.t2>self.t1 and self.arr[self.t2-1]==-1:
            self.t2-=1
            self.arr[self.t2]=x
        else:
            print("Already elemets of st1 present")
    def pop1(self):
        if self.t1==-1:
            return
        self.arr[self.t1]=-1
        self.t1-=1
        
    def pop2(self):
        if self.t2==self.size:
            return
        self.arr[self.t2]=-1
        self.t2+=1
        
    def display(self):
        print(self.arr)
        
tsa = TwoStackArray()
tsa.push1(1)
tsa.push1(2)
tsa.push2(10)
tsa.push2(20)
tsa.push2(30)
tsa.push2(10)
tsa.push2(10)
tsa.display()

        
        

