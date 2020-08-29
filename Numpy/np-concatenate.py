import numpy as np

row_1, row_2, column = map(int, input().strip().split(' '))

arr_1 = np.array([input().strip().split(' ') for _ in range(row_1)], int)
arr_2 = np.array([input().strip().split(' ') for _ in range(row_2)], int)

print(np.concatenate((arr_1, arr_2), axis=0))