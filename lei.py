import numpy as np
import sys
from Input_reader import Input_reader



if __name__ == "__main__":
    input = Input_reader(sys.argv[1])
    sorted_books = sorted(input.books, key=lambda book: book.score, reverse=True)
    sorted_libraries = sorted(input.libraries, key=lambda lib: (lib.duration, -lib.limits))
    day = 0
    isVisited = np.zeros(shape=(input.num_books))
    output_libs = []

    for l in sorted_libraries:
        finish_day =  day + l.duration
        available_day = input.num_days - finish_day
        num_books = available_day * l.limits
        count = 0
        books = sorted(l.books, key=lambda book: input.dict_books[book].score, reverse=True)
        for b in books:
            if isVisited[b] == 0:
                isVisited[b] = 1
                count += 1
                l.output.append(b)
                if count >= num_books:
                    break
        day = finish_day + 1
        output_libs.append(l)
        if day > input.num_days:
            break
    print(len(output_libs))
    for l in output_libs:
        print(l.id, len(l.output))
        for i in l.output:
            print(i, end=" ")
        print()
