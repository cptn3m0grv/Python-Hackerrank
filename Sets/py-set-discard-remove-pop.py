n = int(input())
s = set(list(map(int, input().split())))
for _ in range(int(input())):
    choice=input().split()
    if choice[0]=="pop" :
        s.pop()
    elif choice[0]=="remove" :
        s.remove(int(choice[1]))
    elif choice[0]=="discard" :
        s.discard(int(choice[1]))
            
print(sum(s))