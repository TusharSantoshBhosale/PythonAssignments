class BookStore:

    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print("Book Name is : ",self.Name)
        print("Author Name is : ",self.Author)
        print("Number of Books is : ",BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()