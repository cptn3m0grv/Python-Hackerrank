lines, row = map(int, input().split())

data = [input() for _ in range(lines)]

index = int(input())

for line in sorted(data, key=lambda line: int(line.split()[index])):
    print(line)