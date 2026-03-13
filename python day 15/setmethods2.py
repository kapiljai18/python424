# # # set-> issuperset(), 

# # x={6,89,45,34,90}
# # print(x)

# # # add element
# # # print(x[-1])  # not follows index
# # x.add(100) # adds new element in anywhere
# # print(x)
# # x.add(90) # not added but no error cause set shows without duplicates
# # print(x)

# # # x.add(11,12)  # TypeError: set.add() takes exactly one argument (2 given)
# # # x.add([11,12])  #TypeError: unhashable type: 'list'
# # # x.add([11],[12]) # TypeError: set.add() takes exactly one argument (2 given)
# # x.add((11,12))
# # print(x)

# # # x.update(200) #TypeError: 'int' object is not iterable
# # y={1,2}
# # x.update(y) # we can merge 2 sets by using update method
# # print(x)

# # colors={"red","green","pink","orange"}
# # print(colors)

# # # wap to chnange red colour to light red
# # colors_new=list(colors)
# # print(colors_new)
# # i=colors_new.index("red")
# # colors_new[i]="light red"
# # print(colors_new)
# # colors_new1=set(colors_new)
# # print(colors_new1)

# # wap to show give unique elements from bellow given list
# myList=[12,12,45,23,78,45,1,1,1]
# print(myList)
# # new_mylist=list(set(myList))
# # print(new_mylist)

# # or using loop
# new_list=[]
# for i in myList:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# set comprehension
# # wap to create myset and add number elements as enetered count
# myset=set()
# count=int(input("enter count: "))
# for i in range(count):
#     number=int(input(f"enter {i+1} number: "))
#     myset.add(number)
#     # myset.update(number) # error
# print(myset)

# # comprehension way
# count=int(input("enter count: "))
# myset1={int(input(f"enter {i+1} number: ")) for i in range(count)}
# print(myset1)
# print({i for i in range(10,0,-1)}) #error -> unordered 
# print([i for i in range(10,0,-1)])

# x={12,-324,56,343,-5,35}
# # wap to show only +numbers from above set use comprehension
# print({i for i in x if i>0})



# # wap to show sum of elements of below list
# mylist=[12,3,4,5,11]
# sum=0
# for i in mylist:
#     sum=sum+i
# print(sum)

# # wap to show cube of above elements
# print([i**3 for i in mylist])

# i=10
# while i>=1:
#     print(i)
#     i+=1    # infinite loop
