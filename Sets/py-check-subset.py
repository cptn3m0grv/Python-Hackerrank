# Enter your code here. Read input from STDIN. Print output to STDOUT
# t = int(input())

# for i in range(t):
#     size1 = int(input())
#     s1 = set(map(int, input().split()))
#     size2 = int(input())
#     s2 = set(map(int, input().split()))
#     count = 0
#     if len(s1) >= len(s2):
#         for j in s1:
#             if j in s2:
#                 count = count + 1
#         print(count == len(s2))
#     else:
#         for j in s2:
#             if j in s1:
#                 count = count + 1
#         print(count == len(s1))
                
t = int(input())

for i in range(t):
    size1 = int(input())
    s1 = set(map(int, input().split()))
    size2 = int(input())
    s2 = set(map(int, input().split()))
    print(s1.issubset(s2))