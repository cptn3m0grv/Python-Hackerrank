m = int(input())
a = set(list(map(int, input().split(" "))))
n = int(input())
b = set(list(map(int, input().split(" "))))

fin = set()
fin.update(a.difference(b), b.difference(a))

for i in sorted(fin):
    print(i)