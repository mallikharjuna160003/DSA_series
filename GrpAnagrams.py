import collections
def GrpAnagram(strs):
    res = collections.defaultdict(list)
    for s in strs:
        counts = [0]*26
        for c in s:
            counts[ord(c)-ord('a')]+=1
        
        res[tuple(counts)].append(s)
        print(res)
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]

print(GrpAnagram(strs))
