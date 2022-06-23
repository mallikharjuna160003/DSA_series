def BS(list1, key):
    n = len(list1)
    start = 0
    last = n-1
    while start <= last:
        mid = (start + last)//2
        
        if( list1[mid] == key ):
            return "found"
        elif list1[mid] > key:
            last = mid - 1
        elif list1[mid] < key:
            start = mid + 1
       

list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 32  
print(BS(list1,n))
            
