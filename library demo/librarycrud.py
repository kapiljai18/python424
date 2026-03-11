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
        if len(books)>0:
            old_book_title=input("Enter book title to update: ").capitalize()
            if old_book_title in books:
                new_title=input("enter books new title to update: ").capitalize()
                books[books.index(old_book_title)]=new_title.capitalize()
                print(f"{old_book_title} book title updated successfully to {new_title}")
            else:
                print(f"{old_book_title} book title not found, try again!!!")
        else:
            print("No books available , so first add the books!!!")
    elif choice==4:
        if len(books)>0:
            old_book_title=input("Enter book title to delete: ").capitalize()
            if old_book_title in books:
                books.remove(old_book_title.capitalize())
                print(f"{old_book_title} book deleted successfully")
            else:
                print(f"{old_book_title} book title not found, try again!!!")
        else:
            print("No books available , so first add the books!!!")
    elif choice==5:
        print("Thank you for using our services !!!")
        break