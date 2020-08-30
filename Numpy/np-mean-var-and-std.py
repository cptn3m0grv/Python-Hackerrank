import numpy as np
row, column = map(int, input().strip().split(' '))
np.set_printoptions(sign=' ', legacy = '1.13')
arr = np.array([input().strip().split(' ') for _ in range(row)], int)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr))