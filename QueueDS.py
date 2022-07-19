queue = []
def insert(data):
    queue.append(data)

def pop():
    return queue.pop(0)

for i in range(10):
    insert(i)
for i in range(10):
    print(pop())
    
