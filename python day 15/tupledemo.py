# tuple: collection of different data elements enclosed into () parenthesis
# it is sequence ,index follows, ordered but it is immutable means cant perform crup oerations

# my_tuple=(3,45,64,6764,34,100)
# print(my_tuple)

# # index
# print("first element",my_tuple[0])
# print("last element",my_tuple[-1])

# #slicing
# print(my_tuple[::-1])
# print(my_tuple[2:5])

# # indexing
# tuple1=(1,2,3)
# tuple2=(4,5,6)
# print(tuple1+tuple2)
# # print(tuple1+100)  # error its not tuple so no concatination

# # tuple function
# tuple3=(1,5,4,2,3)
# print(sorted(tuple3))
# print(sorted(tuple3)[::-1])
# print(sorted(tuple3,reverse=True))

# # tuple methods : index(),count()
# tuple4=("hello","red","orange","green",1000,300,700)
# # print(tuple4.index(3)) # valueerror : if element not present then valueerror
# print(tuple4.index(300))
# print(tuple4.index(700))

# immutability 
# tuple4[0]="welcome" # typeerror : 'tuple' object does not support item assignment
# print(tuple4)

# traversing of tuple
# my_tup=(100,200,300,400,1,2,3)
# for i in my_tup:
#     print(i)

# # reverse
# for i in my_tup[::-1]:
#     print(i)

# # ascending
# for i in sorted(my_tup):
#     print(i)

# # descending
# for i in sorted(my_tup)[::-1]:
#     print(i)