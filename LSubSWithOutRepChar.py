def lengthOfLongestSubstring(s):   #with out repeating charaters
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            
            charSet.remove(s[l])
            print(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res,r-l+1)
    print(charSet)
    return res

s = "abcabbca"
print(lengthOfLongestSubstring(s))
