from itertools import combinations
N = int(input())
l = input().split()
k =int(input())
count = 0
for i in list(combinations(l, k)):
    if 'a' in i:
        count = count + 1
        
print("{0:.3f}".format(count/len(list(combinations(l, k)))))