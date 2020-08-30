import numpy as np

n = list(map(float,input().strip().split(' ')))
m = input()
print(np.polyval(n,int(m)))