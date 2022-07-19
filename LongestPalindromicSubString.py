def LongestPalindromicSubString(str1):
    max_len = 1
    st=0
    end=0
    n= len(str1)
    
    #for odd length string
    for i in range(n):
        l,r=i,i
        while(l>=0 and r<n):
            if(str1[l]==str1[r]):
                l-=1
                r+=1
            else:
                break
        length = r-l-1
        if(length>max_len):
            max_len=length
            st =l+1
            end = r-1
       
    #for even length string
    for i in range(n):
        l,r=i,i+1
        while(l>=0 and r<n):
            if(str1[l]==str1[r]):
                l-=1
                r+=1
            else:
                break
        length = r-l-1
        if(length>max_len):
            max_len=length
            st =l+1
            end = r-1

    return str1[st:max_len]

print(LongestPalindromicSubString("fababaf"))

            
