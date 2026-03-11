# list1=[22,44,66,77]
# print(list1)

# # opeartion
# x=[1,2,3]
# y=[4,5,6]
# print(x+y)
# # print(x+100)  $ TypeError: can only concatenate list (not "int") to list
# x.append(100)
# print(x)

# x[2]=222
# print(x)

#methods
# add elements into list append(), insert()
color=[]
print(color)
color.append("red")
print(color)
color.append("pink")
print(color)
# color.append("blue","green")  # TypeError: list.append() takes exactly one argument (2 given)
color.append(["blue","green"])
print(color)
print(color[-1])
print(color[2])
color.append(("cyan","grey"))
print(color)
color.append({"black","yellow"})
print(color)
color.append({"#ffffff":"white"})
print(color)

# update last element
color[-1]="maroon"
print(color)

# add element by using insert
color.insert(0,"orange")  # it add the new element into 0 index and previous one shifts ahead
print(color)
print(len(color))
color.insert(11,"cream")
print(color)

print(color.index("cream"))

# delete element   : .pop(), .remove(), del
color.pop() # removes the last element  
print(color)
color.pop(2) # removes the element on the given index number
print(color)
color.remove("red") # removes the given element if it is present in the list otherwise gives error
print(color)
del color[0]   # uses index number to delete element
print(color)


# traversing the list
for i in color:
    print(i)