from collections import deque











#implement stack using queue
def enque(q,data):
    q.append(data)

def delet(q):
    return q.pop()

q = deque()
enque(q,10)
enque(q,2)
enque(q,1)
enque(q,5)
print(delet(q))
