# importing required function
from avg import avg
import math
x= math.e

info = []  # list for storing info of students


# fun for adding student info
def student(name, marks, gender="M"):
    global info
    av_mark = avg(marks)  # calling imported fun
    info.append([name, gender, av_mark])


# taking repeated input
for i in range(1):
    name = input("enter name : ")
    gender = input("    enter the gender(M/F) :")
    marks = []
    # loop for taking marks info
    for j in range(3):
        marks.append(int(input("   enter mark : ")))

    student(name, marks ,gender)

print(info)
