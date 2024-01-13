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
if __name__ == "__main__":
     # Create Books
    book1 = book(1, "The Catcher in the Rye", "J.D. Salinger")
    # Create Members
    member1 = member(101, "John Doe")
    # Create Library
    library = Library()
    # Add Books to the Library
    library.add_book(book1)
    # Add Members to the Library
    library.add_member(member1)