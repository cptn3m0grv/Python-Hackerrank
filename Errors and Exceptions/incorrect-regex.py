import re

def isValid(reg):
    try:
        re.compile(reg)
    except re.error:
        return False

    return True

if __name__ == '__main__':
    for _ in range(int(input())):
        print(isValid(input()))
    