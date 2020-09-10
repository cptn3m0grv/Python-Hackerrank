if __name__ == '__main__':
    ls = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls.append([name, score])
    
    second_highest = sorted([marks for name, marks in ls])[1]

    for name, marks in sorted(ls):
        if marks == second_highest:
            print(name)