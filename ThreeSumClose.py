def ThreeSumClose(arr,target):
    newarr = []
    for i in range(len(arr)):
         for j in range(i+1,len(arr)):
             for k in range(j+1,len(arr)):
                 newarr.append([arr[i],arr[j],arr[k]])
   
    max1 = -9999
    ind = -99999
    for i,ele in enumerate(newarr):
        if sum(ele)<=target:
            max1 = max(sum(ele),max1)
            ind = i
    print(newarr[ind],max1)

arr = [-3,-7,2,5,6,1]
target =0
Test(arr,target)
    
    
    
    
