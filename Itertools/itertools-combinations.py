# itertools-combinations
from itertools import combinations
word, size = input().split()
word = list(word)
word.sort()
for i in range(1, int(size)+1):
    li = list(combinations(word, i))
    for j in li:
        print(''.join(j))