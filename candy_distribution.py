def candy(ratings, size):
    candies = [1]*(size)
    print(candies)
    flag = True
    while flag:
        flag = False
        for i in range(size):
            if i!=(size-1) and ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1]+1
                flag = True
            if i>0 and ratings[i] > ratings[i-1] and candies[i] <=candies[i-1]:
                candies[i] = candies[i-1]+1
                flag = True
    sum1 = 0
    print(candies)
    for i in range(size):
        sum1+=candies[i]

    return sum1
        

l2 = [1,2,3]
print(candy(l2,len(l2)))
