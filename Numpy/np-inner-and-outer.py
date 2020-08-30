import numpy as np
arr_1 = np.array([input().strip().split(' ')], int)
arr_2 = np.array([input().strip().split(' ')], int)
print(np.inner(arr_1, arr_2)[0][0])
print(np.outer(arr_1, arr_2))