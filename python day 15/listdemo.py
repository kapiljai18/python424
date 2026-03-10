# list : collection of different data elements enclosed into []
# it is sequence , index follows, ordered and it is mutable means it cant be perform crud 

# create list
list1=[]
print(list1,type(list1))
list2=[100]
print(list2,type(list2))
list3=["hellio",100,True,110j,None,(100,200)]
print(list3,type(list3))

# index
print(list3[0])
print(list3[-1])

# mutable
list3[-1]=555
print(list3)