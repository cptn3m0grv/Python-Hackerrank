import numpy as np
row, column = map(int, input().strip().split(' '))
arr = np.array([input().strip().split(' ') for _ in range(row)], int)
print(np.prod(np.sum(arr, axis=0)))