def result(arr,k):
    k = len(arr)-k
    
    def quick_select(l,r):    
        pivot,p = arr[r],l
        for i in range(l,r):
            if arr[i] <= pivot:
                arr[p],arr[i]=arr[i],arr[p]
                p+=1
        arr[p],arr[r] = arr[r],arr[p]

        if p > k: return quick_select(l,p-1)
        elif p < k: return quick_select(p+1,r)
        else: return arr[p]
        
    return quick_select(0,len(arr)-1)




arr = [3,2,1,5,6]
k=4
print(result(arr,k))
