if __name__ == '__main__':
    n = int(input())
    inp = list(map(int, input().strip().split()))[:n]
    inp_tuple = tuple(inp)
    print(hash(inp_tuple))