class BookStore:
    # Class variable
    NoOfBooks = 0

    # Constructor
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        # Increment class variable when a new object is created
        BookStore.NoOfBooks += 1

    # Instance method to display details
    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


# Example usage
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()   # Linux System Programming by Robert Love. No of books: 1

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()   # C Programming by Dennis Ritchie. No of books: 2
