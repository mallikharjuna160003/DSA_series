stack = []
def push(stack,data):
    stack.append(data)

def pop(stack):
    return stack.pop()

for i in range(4):
    push(stack,i)

for i in range(4):
    print(pop(stack))
