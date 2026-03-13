fruits=["apple","grapes","banana","kiwi","watermelon"]
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)

price=[200,300,400,500]
fruits.extend(price)
print(fruits)

j=1
while j<=10:
    if j == 5:
        j+=1
        pass
    else:
        print(j)
        j+=1
print("while outside")