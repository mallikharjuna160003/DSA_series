def insertion_sort(list1):
    n = len(list1)

    for i in range(1,n):
        j = i-1
        next_elem = list1[i]
        while( j >=0) and (list1[j]>next_elem):
            list1[j+1] = list1[j]
            j -= 1
        list1[j+1] = next_elem
    return list1

list1 = [19,2,31,45,30,11,121,27]
print(insertion_sort(list1))
        
            
