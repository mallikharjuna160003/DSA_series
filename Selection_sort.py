def selection_sort(list1):
    n = len(list1)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if( list1[min_i] >list1[j]):
                min_i = j
                
        list1[i],list1[min_i]=list1[min_i],list1[i]

    return list1

l1 = [19 , 2 ,31, 45, 30, 11, 121, 27]
print(selection_sort(l1))
        
            
