def merge(leftA,rightA):
    res = []
    while(len(leftA)!=0) and (len(rightA) != 0):
        if leftA[0]<rightA[0]:
            res.append(leftA[0])
            leftA.remove(leftA[0])
        else:
            res.append(rightA[0])
            rightA.remove(rightA[0])
            
    if len(leftA) == 0:
        res += rightA
    else:
        res += leftA

    return res

def mergesort(list1):
    if len(list1) <= 1:
        return list1
    mid = len(list1)//2
    leftarr = list1[:mid]
    rightarr = list1[mid:]
    leftarr = mergesort(leftarr)
    rightarr = mergesort(rightarr)
    return list(merge(leftarr,rightarr))

l1 = [64, 34, 25, 12, 22, 11, 90]
print(mergesort(l1))
