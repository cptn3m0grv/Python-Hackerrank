# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

t = int(input())

for i in range(t):
    nC, qU = int(input()), deque(map(int, input().split()))
    
    for cL in reversed(sorted(qU)):
        if qU[0] == cL:
            qU.popleft()
        elif qU[-1] == cL:
            qU.pop()
        else:
            print("No")
            break
    else:
        print("Yes")