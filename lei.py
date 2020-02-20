import numpy as np
import sys
from Reader import Reader
from Book import Book
from Library import Library


if __name__ == "__main__":
    file = Reader(sys.argv[1])
    print(file.nextInt())