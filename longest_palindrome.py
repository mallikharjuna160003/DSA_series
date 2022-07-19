def LongestPalindrome(str1):
    HMap = {}
    for ele in str1:
        HMap[ele]=HMap.get(ele,0)+1
    res=0
    even=True
    for k,v in HMap.items():
        if v%2==0:
            res+=v
        else:
            res+=v-1
            even=False
    if(even):
        print("even palindrome length",res+1)
    else:
        print("odd palindrome length",res+1)  
   
            
            
LongestPalindrome("abccccdd")
