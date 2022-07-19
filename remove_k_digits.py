def removeKdigits(nums, k):
    stack = []
    for c in nums:
        while stack and stack[-1]>c and k>0:
            k-=1
            stack.pop()
        stack.append(c)
    stack = stack[:len(stack)-k]
    str1  = "".join(stack)
    return str(int(str1)) if str1 else "0"
k=1
print(removeKdigits("372181",k))
