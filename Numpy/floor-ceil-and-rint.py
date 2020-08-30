import numpy as np

arr = list(map(float, input().strip().split(' ')))
np.set_printoptions(sign=' ')
narr = np.array(arr, dtype=np.float)
print(np.floor(narr))
print(np.ceil(narr))
print(np.rint(narr))