student=[["id","name","grade"],[1,"ravi","C"],[2,"mitesh","B"]]
# print(student)
# print(student[0])
# print(student[1])
# print(student[2])

# for i in student:
#     print(i)

# # find student name and grade whose id is 2
# print("student id 2 name is",student[2][1],"and grade is",student[2][2])

# find studwnt id, name and grade by enterig student id
id=int(input("enter student id to find name and grade: "))
flag=True
for i in student:
    if i[0]==id:
        flag=True
        print("ID:",i[0])
        print("Name:",i[1])
        print("Grade:",i[2])

if flag==False:
    print("id not found, Try again!!!")