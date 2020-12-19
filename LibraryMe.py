print("Welcome To Biblio Library")


class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendbookdict = {}

    def displayBooks(self):
        print(f"We have the following books in {self.name} library:\n")
        for books in self.booklist:
            print(books)

    def lendBook(self, name, book):
        if book not in self.lendbookdict.keys():
            self.lendbookdict.update({book: name})
            print(
                f"We have succesfully lend the book for you. You can now tale it.\nMake sure to return it within 30 days at the max or you have to pay a fine of Rs. 5 per day of extra usage")
        else:
            print(
                f"Sorry! This book is already borrowed by {self.lendbookdict[book]}")

    def addbook(self, name, book, author):
        self.booklist.append(book)
        print("Congratulations! We have successfully added this book to the library")

    def returnbook(self, book):
        self.lendbookdict.pop(book)

    @classmethod
    def from_slash(cls, string):
        return cls(*string.split("by"))


if __name__ == "__main__":
    Sanni = Library(["Sherlock Holmes by Sir Arthur Conan Doyle", "Feluda Somogro by Satyajit Ray",
                     "Roads To Nanital by Ruskin Bond"], "Biblio")
while(True):
    print(
        f"Welcome to the {Sanni.name} library. Enter your choice to continue")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")
    user_choice = input()
    if user_choice not in ['1', '2', '3', '4']:
        print("Please enter a valid input")
        continue
    else:
        user_choice = int(user_choice)
    if user_choice == 1:
        Sanni.displayBooks()
    elif user_choice == 2:
        name = input("Please tell us your name:\n")
        book = input("Please tell us the name of the book you wish to lend:\n")
        # if book == Sanni.booklist[0]:
        Sanni.lendBook(name, book)

    elif user_choice == 3:
        name = input("Please tell us your name:\n")
        book = input("Please tell us the name of the book you wish to add\n")
        author = input("Please tell us the name of the author of the book:\n")
        Sanni.addbook(name, book, author)
    elif user_choice == 4:
        book = input(
            "Please tell us the name of the book you want to return:\n")
        Sanni.returnbook(book)
        print("Thanks for returning the book! Hope you enjoyed it")

    print("Enter c to continue and q to exit")
    user_choice2 = ""
    while(user_choice2 != "c" and user_choice2 != "q"):
        user_choice2 = input()
        if user_choice2 == "q":
            print("Thanks for visiting Biblio Library! Do come again")
            exit()

        elif user_choice2 == "c":
            continue
