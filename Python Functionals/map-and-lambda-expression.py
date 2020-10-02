cube = lambda x: pow(x, 3) # or x*x*x will also work 

def fibonacci(n):
    fb = [0, 1]
    for i in range(2, n):
        fb.append(fb[i-1] + fb[i-2])
    return fb[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))