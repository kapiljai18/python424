# # methods: count, find, replace, join,index, split, splitline, zfill
# #iterate string
# name="Itvedant"
# # for i in name:
#     # print(i)

# # reverse string
# # print("reverse string:",name[::-1])
# newstr=""

# for i in name:
#     newstr=i+newstr
# print(newstr)


# wap to newstrng without vowels
# withoutvowels=""
# for i in name:
#     if i not in "aeiouAEIOU":
#         withoutvowels=withoutvowels+i
# print(withoutvowels)

# wap to print num of occurances of entered characters from entered string
# str=input("enter string: ")
# char=input("enter charactor :")
# count=0
# for i in str:
#     if char==i:
#         count+=1
    
# print(f"{char} character count in {str} is {count}")


# wap to print num of occurances of entered word from entered string
# str=input("enter string: ")
# checkstr=input("enter word to find and show count ")
# check=""
# count=0
# for i in range(len(str)):
#     # print(i,str[i])
#     k=i
#     for j in range(len(checkstr)):
#         try:
#             check+=str[k]
#             k+=1
#         except:
#             None
#     if check==checkstr:
#         count+=1
#     check=""
# if count!=0:
#     print(f"{checkstr} found in {str} and count is {count}")
# else:
#     print(f"{checkstr} not found in {str}")


