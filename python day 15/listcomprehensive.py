# # methods -> index(),count(),append(),insert(),pop(),remove(),del,reverse(),sort(),extend(),copy(),clear()
# for i in range(1,11):
#     print(i,end=" ")


# # list comprehension
#syntax->[output for iterable_variable in sequence_object if condition]

# # print 1 to 10
# print([i for i in range(1,11)])

# # print square of 1 to 10 numbers 
# print([i*i for i in range(1,11)])

# # print even numbers from 1 to 10
# for i in range(1,11):
#     if i%2==0:
#         print(i,end=" ")

# print([i for i in range(1,11) if i%2==0])

# # create an mylist add numbers as per count enter  # very important question in interview

# # 1
# mylist=[]
# count=int(input("enter count for numbers: "))
# for i in range(count):
#     number=int(input(f"enter {i+1} number: "))
#     mylist.append(number)
# print(mylist)

# # 2
# mylist=list()
# count=int(input("enter count for numbers: "))
# for i in range(count):
#     number=int(input(f"enter {i+1} number: "))
#     mylist.append(number)
# print(mylist)

# # 3 comprehensive way
# count=int(input("enter count for numbers: "))
# mylist_new=[int(input(f"enter {i+1} number: ")) for i in range(count)]
# print(mylist_new)

# # wap to show even and odd numbers separately
# 1
# mylist=[12,4,2,67,256,600,2]
# even=[]
# odd=[]
# for i in mylist:
#     if i%2==0:
#         even.append(i)

#     else:
#         odd.append(i)
# print("even numbers: ",even)
# print("odd numbers: ",odd)

# # 2 comprehensive way 1
# mylist=[12,4,2,67,256,600,2]
# even=[a for a in mylist if a%2==0]
# odd=[a for a in mylist if a%2!=0]
# print("even numbers: ",even)
# print("odd numbers: ",odd)

# # 3 comprehension way 2
# mylist=[12,4,2,67,256,600,2]
# even=[]
# odd=[]
# [even.append(i) if i%2==0 else odd.append() for i in mylist]
# print("even numbers: ",even)
# print("odd numbers: ",odd)

