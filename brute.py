import numpy as np
import sys
from Input_reader import Input_reader
import itertools
import time



if __name__ == "__main__":
    input = Input_reader(sys.argv[1])
    sorted_books = sorted(input.books, key=lambda book: book.score, reverse=True)
    max_score = 0
    for lib in input.libraries:
        lib.books = sorted(lib.books, key=lambda book: input.dict_books[book].score, reverse=True)
    iter = 0
    for p in itertools.permutations(input.libraries):
        iter += 1
        if (iter > 100):
            break
        day = 0
        isVisited = np.zeros(shape=(input.num_books))
        output_libs = []
        score = 0
        for l in p:
            finish_day =  day + l.duration
            available_day = input.num_days - finish_day
            num_books = available_day * l.limits
            count = 0
            l.output = []
            for b in l.books:
                if isVisited[b] == 0:
                    isVisited[b] = 1
                    count += 1
                    l.output.append(b)
                    score += input.dict_books[b].score
                    if count >= num_books:
                        break
            day = finish_day + 1
            output_libs.append(l)
            if day > input.num_days:
                break
        
    # print(len(output_libs))
    # for l in output_libs:
    #     if len(l.output) == 0:
    #         continue
    #     print(l.id, len(l.output))
    #     for i in l.output:
    #         print(i, end=" ")
    #     print()
    output_libs = [lib for lib in output_libs if len(lib.output) > 0]
    f = open("a.txt", "w")
    f.write(str(len(output_libs)) + "\n")
    for l in output_libs:
        print(str(l.id) + " " + str(len(l.output)) + "\n")
        f.write(str(l.id) + " " + str(len(l.output)) + "\n")
        for i in l.output:
            f.write(str(i) + " ")
        f.write("\n")
    f.close()
