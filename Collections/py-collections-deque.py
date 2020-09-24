from collections import deque

num = int(input())
d = deque()
for i in range(num):
    ip = input().strip().split(' ')
    if("append" in ip):
        d.append(int(ip[1]))
    elif(ip[0] == "appendleft"):
        d.appendleft(int(ip[1]))
    elif(ip[0] == "pop"):
        d.pop()
    elif(ip[0] == "popleft"):
        d.popleft()

for j in range(len(d)):
    print(d[j], end=" ")