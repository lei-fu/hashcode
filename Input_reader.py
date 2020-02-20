from Reader import Reader
from Book import Book
from Library import Library

class Input_reader:
    def __init__(self, file_name):
        file = Reader(file_name)
        self.num_books, self.num_libraries, self.num_days = file.nextInt(), file.nextInt(), file.nextInt()
        self.books = []
        self.dict_books = {}
        self.libraries = []
        for i in range(self.num_books):
            temp = file.nextInt()
            self.dict_books[i] = Book(i, temp)
            self.books.append(Book(i, temp))
        for i in range(self.num_libraries):
            num_books_lib = file.nextInt()
            duration, limits = file.nextInt(), file.nextInt()
            books_lib = []
            for j in range(num_books_lib):
                books_lib.append(file.nextInt())
            self.libraries.append(Library(i, books_lib, duration, limits))

    def __str__(self):
        return str(self.num_libraries) + " " + str(self.num_days)
    
