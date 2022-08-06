class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def display_books_available(self):
        print("Here is the list of books: ")
        for i in self.books:
            # a = list(map(str, i.split()))
            print('-->'+i)

    def Book_Issue(self,bookName):
        if bookName in self.books:
            print(f"\nThe {bookName} book is issued to you for next 30 days. Happy Reading!...\n\n")
            self.books.remove(bookName)
        else:
            print("\nEither this book doesn't exist in our Library or already issued to someone.\n\n")
            
    
    def bookReturn(self, bookName):
        self.books.append(bookName)
        print("\n-------Return Successful---------\n\n")
        

# class Student:
#     def bookReturn(self):
#         self.book = input("Name of the book, you are willing to return: ")
#         return self.book


if __name__=='__main__':
    cl = Library(['Python','Django','JS','C','C++','HTML','CSS'])

    while True:
        msg = '''==========Honour to Welcome you to the Library==========
        Select actions using the numbers
        1) Show the list of Available Books
        2) Want to borrow a book
        3) Want to return a book
        4) Done by myside I wanna exit'''
        print(msg)
        a = input("Enter here: ")

        if a == '1':
            cl.display_books_available()
        elif a == '2':
            bn = input("Type the name of the book: ")
            cl.Book_Issue(bn)
        elif a == '3':
            bn = input("Type the name of the book: ")
            cl.bookReturn(bn)
        else:
            print("\n---------------Thanks for the visit...----------------")
            exit()
            
        

# --------------------------NOT FINISHED YET-----------------------------------
