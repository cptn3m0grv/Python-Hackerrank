lower = []
upper = []
od = []
ev = []
for ch in sorted(input()):
    if ch.isalpha():
        if ch.islower():
            lower.append(ch)
        elif ch.isupper():
            upper.append(ch)
    else:
        if int(ch)%2==0:
            ev.append(ch)
        else:
            od.append(ch)
                
print("".join(lower+upper+od+ev))