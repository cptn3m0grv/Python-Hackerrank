lines, width = input().split(" ")

lines = int(lines)
width = int(width)

count = 0
bcount = 0

if((lines%2 != 0) and width == 3*lines):
    for i in range(1, lines//2 + 1):
            str = ".|."*(i+count)
            str = str.center(width, "-")
            print(str) 
            count = count + 1
    bcount = count - 1
    
    print("WELCOME".center(width, "-"))

    for i in range(lines//2, 0, -1):
        str = ".|."*(i+bcount)
        str = str.center(width, "-")
        print(str)
        bcount = bcount - 1