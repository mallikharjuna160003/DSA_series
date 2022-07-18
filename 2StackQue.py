def push(stack,data ):
    stack.append(data)
    
def pop(stack):
    if len(stack)==0:
        return "Stack is empty"
    else:
        return stack.pop()

temp = []
stack = []

def enque(data):
    push(stack,data)
    
def deque():
    for i in range(len(stack)):
        push(temp,pop(stack))
        
    ans = pop(temp)
    for i in range(len(temp)):
        push(stack,pop(temp))
    return ans

        
enque(10)
enque(20)
enque(30)
enque(40)
print(deque())
enque(50)
print(deque())
print(deque())
enque(60)
print(deque())
print(deque())
print(stack)










