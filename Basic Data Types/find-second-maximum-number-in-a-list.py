# Finding the runner up
n = int(input())

scores = list(map(int, input().strip().split()))[:n]

first = max(scores) 

while max(scores) == first:
    scores.remove(max(scores))

print(max(scores))