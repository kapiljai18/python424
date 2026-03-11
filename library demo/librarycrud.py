books=[]
while True:
    print("----------library management-----------")
    print("1.Add Books\n2.Show Books\n3.Update Books\n4.Delete Books\n5.Exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        title=input("Enter book title: ").capitalize()
        if title not in books:
            books.append(title)
            print(f"{title} Book added successfully")
        else:
            print(f"{title} Book is already exists so add another book")
    elif choice==2:
        if len(books)==0:
            print("no books available, try again!!")
        else:
            print("available books are :",books)
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        print("Thank you for using our services !!!")
        break