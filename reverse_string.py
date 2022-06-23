def rev(s):
    n = len(s)
    i = 0
    l1 = list(s)
    temp = l1[i]
    l1[i] = l1[n-1-i]
    l1[n-1-i] = temp
    s1 = "".join(l1)
    return s1


def reverse1(s):
    n = len(s)
    spaces = [' ']
    words = []
    i = 0
    while i < n:
        if s[i] not in spaces:
            word_start = i
            while i < n and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
            
        i+=1
        
    return " ".join(map(rev,words[::-1]))
print(reverse1("This is Monk"))

