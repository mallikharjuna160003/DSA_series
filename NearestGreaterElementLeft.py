def NGEL(arr):
    v = []
    stack = []
    
    for i in range(len(arr)):
        if(len(stack)==0):
            v.append(-1)
        elif(len(stack)>0 and arr[i]<stack[-1]):
            v.append(stack[-1])
        elif(len(stack)>0 and arr[i]>stack[-1]):
            while(len(stack)>0 and arr[i]>stack[-1]):
                stack.pop()
            if(len(stack)==0):
                v.append(-1)
                
            else:
                v.append(stack[-1])
        stack.append(arr[i])
    print(v)

arr = [100,80,60,70,60,75,85]
NGEL(arr)

