def mutate_string(string, position, character):
    sp = list(string)
    sp[position] = character
    return "".join(sp)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)