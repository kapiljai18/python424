# # dict:- collection of element represented into key, value pair enclosed within {k:v}
# # it follows key indexing and key order and no sitting and it is mutable

# # # create empty dictionary
# # d={}
# # print(d,type(d))
# # d1=dict()
# # print(d1,type(d1))

# # d2={1:1000,2:2000,3:3000,4:4000}
# # print(d2)

# # students details
# d3={"rollno":101,"name":"pooja","grade":"A+"}
# print(d3)
# d4={"subjects":["py","js","html","css"]}
# print(d4)
# # d5={[1,2,3]:[1,4,9]}   # TypeError: unhashable type: 'list'
# d5={(1,2,3):[1,4,9]}
# print(d5)
# d6={(1,2,3):"rahul"}
# print(d6)

# # no operations and no slicing

# # key index
# print(d3["name"])
# print(d4["subjects"])

# print(len(d3))
# print(len(d4))


# crud opeartions on empty dict without using method
books={}
print(books)
books["isbn"]=1111
print(books)
books["isbn"]=5555 # it updates th previous isbn value
print(books)

books["title"]="python"
books["author"]="rossom"
books["price"]=899
print(books)

books["dop","qty"]="12-04-2000",20
print(books)

# change price to 900
books["price"]=900
print(books)

# show book title and price
print(books["title"],books["price"])

# delete the author

del books["author"]
print(books)