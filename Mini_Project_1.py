# Online Library Management System:


# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# RudrakshLibrary = Library(listofbooks, library_name)


# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

'''
Statement:-
The task is to create an “Online Library Management System”. For this, you have to create a library class which includes the following
methods:

Displaybook() : To display the available books
Lendbook(): To lend a book to a user
Addbook(): To add a book in the library
Returnbook(): To return the book in the library.
As you have created a library class, now you will create an object and pass the following parameters in the constructor.

RudrakshLibrary=Library(listofbooks, library_name)

After that, create a main function and run an infinite while loop which asks the users for their input that whether they want to display,
lend, add or return a book.

Optional:-
Maintain a dictionary for the users who own a book. Dictionary should take book name as a key and name of the person as a value. Whenever
you lend a book to a user, you should maintain a dictionary.
'''


class Library:
    def __init__(self, list, name):
        self.BookList = list
        self.name = name
        self.LendDict = {}

    def DisplayBooks(self):
        print(f"We have Follwing books in the Library: {self.name}")
        for book in self.BookList:
            print(book)

    def LendBook(self, user, book):
        if book not in self.LendDict.keys():
            self.LendDict.update({book: user})
            print("Lender-Book Database has been Updated. You can take your book now.")
        else:
            print(f"Book is already been used by {self.LendDict[book]}")

    def AddBook(self, book):
        self.BookList.append(book)
        print("Book has been added to the book list.")

    def ReturnBook(self, book):
        self.LendDict.pop(book)


if __name__ == '__main__':
    rudra = Library(['Python', 'Harry Potter', 'Winner Stands Alone', 'Alchemist', 'C++ Basics', 'Half Girlfriend',
                     'How to read a Person like a Book', 'Chanakya in You'], "Rudraksh Agarwal")
    while(True):
        print(f"Welcome to the {rudra.name} Library.\nEnter your choices to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Enter a valid Choice.")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            rudra.DisplayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to Lend:\n")
            user = input("Enter your name")
            rudra.LendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to Add:\n")
            rudra.AddBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to Return:\n")
            rudra.ReturnBook(book)
        else:
            print(("Not a Valid Option. Please Choose the Valid Options."))

        print("Press q to quit and c to Continue.")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
