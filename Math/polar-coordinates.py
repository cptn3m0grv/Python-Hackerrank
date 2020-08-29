import cmath
x = complex(input())
print("\n".join([str(abs(x)), str(cmath.phase(x))]))