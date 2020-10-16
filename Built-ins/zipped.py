n,x = map(int, input().split())
subjects = []
for i in range(x):
    subjects.append(map(float, input().split()))

for i in zip(*subjects):
    print(sum(i)/len(i))