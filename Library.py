class Library:
    library_name = "Central Library"
    library_address = "21/4 Rajani Sen Road, Kolkata 700030"
    library_categories = ("Thriller", "Science Fiction", "Non Fiction",
                          "Horror", "Mystery", "Adventure", "Comedy", "Religious", "Reference type")

    # def printAll(self):
    #     print(self.printdetails())

    while(True):
        Cont_Query = input("Please choose your action:\nD for displaying all books\nL for lending a book for returning a book\nA for donating a book\nF for paying fine\n\nLibrarian Actions:\nRo to remove a member\nAo to add a member")
        if Cont_Query == "D":
            # print(Feluda.printdetails())
            for b in Books:
                print(b)


class Books(Library):

    def __init__(self, bookName, bookAuthor, bookCategory, bookPrice):
        self.bookName = bookName
        self.bookAuthor = bookAuthor
        self.bookCategory = bookCategory
        self.bookPrice = bookPrice

        def printdetails(self):
            return f"The name of the bool is {self.bookName}.\nThe author is {self.bookAuthor} and\nThe price is {self.bookCategory}\n"


Feluda = Books("Feluda Somogro", "Satyajit Ray", "Adventure", 4678)
Sherlock = Books("The adventures of Sherlock Holmes",
                 "Sir Arthur Conan Doyle", "Adventure", 2999)
Brittanica = Books("The Encyclopedia Brittanica",
                   "James Tytler", "Reference type", 5999)
FaceInDark = Books("A Face In The Dark", "Ruskin Bond", "Horror", 599)
Byomkesh = Books("Byomkesh Somogro",
                 "Sharadindu Bandhopadhay", "Adventure", 2999)
Aboltabol = Books("AbolTabol", "Sukumar Ray", "Comedy", 3599)
