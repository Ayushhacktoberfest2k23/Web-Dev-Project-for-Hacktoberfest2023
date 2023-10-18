class Book:
    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Price: {book.price}, Copies: {book.copies}")

# Creating a bookstore
bookstore = Bookstore()

# Adding some books
bookstore.add_book(Book("Python Programming", "Guido van Rossum", 30, 10))
bookstore.add_book(Book("Java Programming", "James Gosling", 25, 15))
bookstore.add_book(Book("C++ Programming", "Bjarne Stroustrup", 35, 5))

# Displaying all books
print("All Books:")
bookstore.display_books()

# Searching for a book
search_title = "Python Programming"
result = bookstore.search_book(search_title)
if result:
    print(f"\nBook Found - Title: {result.title}, Author: {result.author}, Price: {result.price}, Copies: {result.copies}")
else:
    print(f"\nBook with title {search_title} not found.")
