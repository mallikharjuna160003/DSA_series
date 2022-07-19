class SetDS:   # implementation of Set Data structure using O(1) TC and SC
    def __init__(self):
        self.mask = 0
        
    def add(self,n):
        self.mask = self.mask|(1<<n)
        
    def remove(self,n):
        self.mask = self.mask^(1<<n)
        
    def display(self):
        for bits in range(0,60):
            if(self.mask&(1<<bits)):
                print(bits,end=' ')
        print()
        
        
obj = SetDS()
obj.add(10)
obj.add(20)
obj.add(40)
obj.display()
obj.remove(10)
obj.display()



def Powersets(arr):  #power set for array of integers
    res = []
    n = pow(2,len(arr))
    for ele in range(n):
        subsets = []
        for bit in range(0,ele):
            if(ele&(1<<bit)):
                subsets.append(arr[bit])
        res.append(subsets)
    print(res)

arr = [1,2,3]
Powersets(arr)


            
def SwapNums(A,B):
    print(A,"\t",B)
    A=A^B
    B=A^B
    A=A^B
    print(A,"\t",B)
    
SwapNums(3,4)



def copySetBitInRange(X,Y,start,end):  # copy setbits in a range from Y to X start and end are position -1 of them gives index
    start-=1
    end-=1
    for i in range(start,end+1):
        temp = 1<<i
        if(Y&temp):         #checking for set bits in Y
            X|=(Y&temp)     #copying the set bits by logical OR
    print(X)

copySetBitInRange(44,3,1,5) 
    
        

def PowerSet(str1):  #set of subsequences of a string
    n = pow(2,len(str1)) 
    result = []
    for i in range(1,n):
        x=i
        j=0
        ans=""
        while(x):
            if(x&1):
                ans+=str1[j]
            x=x>>1
            j+=1
        result.append(ans)
    print(result)

str1 = "abc"
PowerSet(str1)



def CountAToBbitFlip(A,B): #converting A to B required bits to be flipped
    count = 0
    exor = A^B
    while(exor):
        if((exor&1)>0):
            count+=1
        exor=exor>>1
    print(count)
    
CountAToBbitFlip(7,15)



def singleSetBit(arr):  # return the numbers the bits contain single bit
    result= {}
    for ele in arr:
        N=ele
        index = 0
        if((ele&(ele-1))==0):
           while(ele):
               if(ele&1):
                   result[N]=index
               ele = ele>>1
               index+=1
    print(result)

arr = [1,3,2,4,8]
singleSetBit(arr)
               


def find2NPlus1(arr):  # return the non repeating num 2N+1 among all repeating twice numbers
    exor = 0
    for ele in arr:
        exor^=ele
    print(exor)

arr = [1,2,4,2,1]
find2NPlus1(arr)

    

def find2NPlus2(arr):   # return the two non repeating num 2N+2 among all repeating twice numbers
    setbitN, unsetbitM = 0,0
    exor=0

    for ele in arr:
        exor^=ele
        
    #finding the right most setbit for partition setbit and unsetbit
    right_setBit = exor&(~(exor-1)) 
    
    for ele in arr:
        if((ele&right_setBit)>0): 
            setbitN^=ele
        else:
            unsetbitM^=ele
    print(setbitN,unsetbitM)

arr = [1,2,1,2,3,4]
find2NPlus2(arr)



def CountSetBits(N):         # return the count of set bits in a number
    count = 0
    while(N):
        if((N&1)>0):
            count+=1
        N=N>>1
    print(count)
    
CountSetBits(15)



def NPowerOf2(N):         #return N^2
    x=N
    j=0
    ans=0
    while(x):
        if(x&1):   # set bits only get multiplied
            ans+=(N<<j)   #ans = 11*2^j + ans
        j+=1
        x=x>>1
    print(ans)
NPowerOf2(10)



def PowerOf2Check(N):     # return check 2^i or not
    if N ==0: return False
    if(N&(N-1)==0):
        return True
    else:
        return False

print(PowerOf2Check(4))


            
