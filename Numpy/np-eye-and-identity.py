import numpy as np

n, m = map(int, input().strip().split(' '))
np.set_printoptions(sign=' ')
print(np.eye(n, m, k=0, dtype=np.float))