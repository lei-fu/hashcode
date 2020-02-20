import numpy as np
import sys
from Reader import Reader
from Book import Book
from Library import Library


if __name__ == "__main__":
    file = Reader(sys.argv[1])
    num_books, num_libraries, num_days = file.nextInt(), file.nextInt(), file.nextInt()
    books = []
    libraries = []
    for i in range(num_books):
        books.append(Book(i, file.nextInt()))
    for i in range(num_libraries):
        num_books_lib = file.nextInt()
        duration, limits = file.nextInt(), file.nextInt()
        books_lib = []
        for j in range(num_books_lib):
            books_lib.append(file.nextInt())
        libraries.append(Library(books_lib, duration, limits))
    for b in books:
        print(b)
    for l in libraries:
        print(l)
