# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
for i, j in groupby(input()):
    print("({}, {})".format(len(list(j)), i), end=" ")