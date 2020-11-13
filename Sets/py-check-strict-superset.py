# Enter your code here. Read input from STDIN. Print output to STDOUT
s1 = set(map(int, input().split()))
ans = []
for i in range(int(input())):
    s2 = set(map(int, input().split()))
    if(len(s2)>=len(s1)):
        ans.append(False)
    else:
        ans.append(s2.issubset(s1))
        
res = True
for i in ans:
    res = res and i
    
print(res)
