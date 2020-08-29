import numpy as np 

row, column = map(int, input().split(' '))
arr = np.array([input().strip().split(' ') for _ in range(row)], int)
print(np.transpose(arr))
print(arr.flatten())