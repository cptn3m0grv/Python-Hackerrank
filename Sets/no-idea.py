# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
n, m = int(n), int(m)

arr = list(map(int, input().split()))
sA = set(map(int, input().split()))
sB = set(map(int, input().split()))

hap = 0

for i in arr:
    if i in sA:
        hap = hap + 1
    
    if i in sB:
        hap = hap - 1
        
print(hap)
        
