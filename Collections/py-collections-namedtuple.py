from collections import namedtuple
tot_students = int(input())
col_name = input()
Students = namedtuple('Students', col_name)
marks = 0
for i in range(tot_students):
    stud = Students(*input().split())
    marks += int(stud.MARKS)
print("{0:.2f}".format(marks/tot_students))