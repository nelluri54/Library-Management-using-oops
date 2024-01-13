class book:
    def __init__(self,bid,btitle,bauthor):
        self.bid=bid
        self.title=btitle
        self.author=bauthor
        self.is_available=True
class member:
    def __init__(self,mid,name):
        self.mid=mid
        self.name=name
        self.borrowed=[]
    def borrow_book(self,book):
        if book.is_available:
            self.borrowed.append(book)
            book.is_available = False
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available for borrowing.")
    def return_book(self, book):
        if book in self.borrowed:
            self.borrowed.remove(book)
            book.is_available = True
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"Error: '{book.title}' is not borrowed by {self.name}.")
    def list_borrowed_books(self):
        print(f"{self.name}'s borrowed books:")
        for book in self.borrowed_books:
            print(f"{book.title} by {book.author}")
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print(f"Error: Book '{book.title}' not found in the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f"Member '{member.name}' removed from the library.")
        else:
            print(f"Error: Member '{member.name}' not found in the library.")

    def list_books(self):
        print("Available books in the library:")
        for book in self.books:
            if book.is_available:
                print(f"{book.title} by {book.author}")

    def list_members(self):
        print("Members of the library:")
        for member in self.members:
            print(f"- {member.name}")
def main():
    library=Library()
    while True:
        print("\nmenu:")
        print("1.create books\n2.create members\n3.add book\n4.remove book\n5.add member\n6.remove_member\n7.list of members\n8.list of books\n9.borrow book\n10.return book\n11.list of borrowed books")
        choice=int(input("\nenter your choice:"))
        if choice==1:
            bid=input("enter book id:")
            bname=input("enter book name:")
            bauthor=input("enter book author:")
            b1=book(bid,bname,bauthor)
        elif choice==2:
            mid=input("enter member id:")
            mname=input("enter member name:")
            m1=member(mid,mname)
        elif choice==3:
            library.add_book(b1)
        elif choice==4:
             library.remove_book(b1)
        elif choice==5:
            library.add_member(m1)
        elif choice==6:
            library.remove_member(m1)
        elif choice==7:
            library.list_members()
        elif choice==8:
            library.list_books()
        elif choice==9:
            m1.borrow_book(b1)
        elif choice==10:
            m1.return_book(b1)
        elif choice==11:
            member.list_borrowed_books
        else:
            break
if __name__ == "__main__":
    main()
        
        
