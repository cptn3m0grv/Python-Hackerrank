if __name__ == '__main__':
    n = int(input())
    ini = []
    for i in range(n):
        inp = input().split(" ")
        if(len(inp) == 3):
            ini.insert(int(inp[1]), int(inp[2]))
        elif(len(inp) == 1):
            if(inp[0] == "print"):
                print(ini)
            elif(inp[0] == "pop"):
                ini.pop()
            elif(inp[0] == "sort"):
                ini.sort()
            elif(inp[0] == "reverse"):
                ini.reverse()
        elif(len(inp) == 2):
            if(inp[0] == "remove"):
                ini.remove(int(inp[1]))
            elif(inp[0] == "append"):
                ini.append(int(inp[1]))
