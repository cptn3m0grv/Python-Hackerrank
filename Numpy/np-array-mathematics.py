import numpy as np

row, column = map(int , input().strip().split(' '))

a = np.array([input().strip().split(' ') for _ in range(row)], int)
b = np.array([input().strip().split(' ') for _ in range(row)], int)

print(np.add(a, b)) 
print(np.subtract(a, b)) 
print(np.multiply(a, b))
print(np.floor_divide(a, b))
print(np.mod(a, b))
print(np.power(a, b))