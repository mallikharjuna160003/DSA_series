def maxheapify(arr,n,i):
    left = 2*i+ 1
    right = 2*i+2
    largest = i
    if(left<n and arr[largest]<arr[left]):
        largest = left
    elif(right<n and arr[largest]<arr[right]):
        largest = right
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        maxheapify(arr,n,largest)
    

def buildheap():
    ar = [4,1,3,5,7]
    n = len(ar)
    for i in range(n//2 -1,-1,-1):
        maxheapify(ar,n,i)
    for i in range(n-1, 0, -1):
        ar[0],ar[i]=ar[i],ar[0]
        maxheapify(ar,i,0)

    print(ar)

buildheap()
