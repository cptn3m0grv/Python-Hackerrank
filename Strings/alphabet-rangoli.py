def print_rangoli(size):
    # your code goes here
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    lis = []
    for i in range(size):
        s ="-".join(alphabets[i:size])
        lis.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print("\n".join(lis[:0:-1]+lis))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)