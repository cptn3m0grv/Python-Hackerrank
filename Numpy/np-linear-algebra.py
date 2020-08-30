import numpy as np
row = int(input())
np.set_printoptions(legacy='1.13')
arr = np.array([input().strip().split(' ') for _ in range(row)], float)
print(np.linalg.det(arr))