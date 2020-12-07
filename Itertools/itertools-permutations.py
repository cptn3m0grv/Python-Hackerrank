# itertools-permutation
from itertools import permutations
word, size = input().split()
size = int(size)
ans = []
for i in list(permutations(word, size)):
    l = ""
    for _ in i:
        l=l+_
    ans.append(l)
    
for _ in sorted(ans):
    print(_)    