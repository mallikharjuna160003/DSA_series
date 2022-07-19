def BS(arr,start,end,value):
    if(start > end):
        return False
    else:
        mid = int((end+start)/2)
        
        if(arr[mid] == value):
            return mid
        elif(arr[mid]>value):
            end = mid
            return BS(arr,start,end,value)
        elif(arr[mid]<value):
            start = mid+1
            return BS(arr,start,end,value)

        
    







arr = [1,2,3,4]
start = 0
end = len(arr)-1
value = 4
print(BS(arr,start,end,value))
