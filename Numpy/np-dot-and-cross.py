import numpy as np

row = int(input())

arr_1 = np.array([input().strip().split(' ') for _ in range(row)], int)
arr_2 = np.array([input().strip().split(' ') for _ in range(row)], int)

print(np.dot(arr_1, arr_2))