# itertools-combinations-with-replacement
from itertools import combinations_with_replacement as cwr
word, size = input().split()
for i in cwr(sorted(word), int(size)):
    print(''.join(i))