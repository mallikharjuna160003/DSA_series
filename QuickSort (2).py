def partition(arr,l,r):
    ptr,pivot = l-1,arr[r]
    for i in range(l,r):
        if arr[i]<=pivot:
            ptr+=1
            arr[i],arr[ptr]=arr[ptr],arr[i]
            
    arr[r],arr[ptr+1] = arr[ptr+1],arr[r]
    return ptr+1
    

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    

arr = [1,3,2,5,6]
n = len(arr)-1
quicksort(arr,0,n)
print(arr)
