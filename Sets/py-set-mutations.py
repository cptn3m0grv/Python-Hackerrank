m = int(input())
a = set(list(map(int, input().split())))
for _ in range(int(input())):
    cmd, n = input().split()
    b = set(list(map(int, input().split())))
    getattr(a, cmd)(b)

print(sum(a))