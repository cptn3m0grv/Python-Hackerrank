from collections import Counter
if __name__ == "__main__":
    str_input = input()
    count = Counter(str_input).items()
    for i in sorted(count, key = lambda x: (-x[1], x[0]))[:3]:
        print(i[0], i[1])