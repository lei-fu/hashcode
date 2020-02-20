from Reader import Reader
from Book import Book
from Library import Library

class Input:
    def __init__(self, file_name):
        file = Reader(file_name)
        self.num_books, self.num_libraries, self.num_days = file.nextInt(), file.nextInt(), file.nextInt()
        self.books = []
        self.libraries = []
        for i in range(self.num_books):
            self.books.append(Book(i, file.nextInt()))
        for i in range(self.num_libraries):
            num_books_lib = file.nextInt()
            duration, limits = file.nextInt(), file.nextInt()
            books_lib = []
            for j in range(num_books_lib):
                books_lib.append(file.nextInt())
            self.libraries.append(Library(books_lib, duration, limits))

    def __str__(self):
        return str(self.num_libraries) + " " + str(self.num_days)