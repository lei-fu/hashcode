import numpy as np
import sys
from Input_reader import Input_reader
import math

def out(output_libs):
    output_libs = [lib for lib in output_libs if len(lib.output) > 0]
    print(len(output_libs))
    for l in output_libs:
        if len(l.output) == 0:
            continue
        print(l.id, len(l.output))
        for i in l.output:
            print(i, end=" ")
        print()


def sort_libs(libs, input, isVisited, day): 
    for l in libs:
        books = sorted(l.books, key=lambda book: input.dict_books[book].score, reverse=True)
        finish_day =  day + l.duration
        available_day = input.num_days - finish_day
        if available_day <= 0:
            l.score= 0
            continue

        num_books = available_day * l.limits
        count = 0
        score = 0
        for b in books:
            if isVisited[b] == 0:
                count += 1
                score += input.dict_books[b].score
                if count >= num_books:
                    break
        l.score = score 

    return sorted(libs, key=lambda lib: 1.0*lib.limits*lib.score/lib.duration, reverse=True)

def main():
    input = Input_reader(sys.argv[1])
    day = 0
    libs = input.libraries
    isVisited = np.zeros(shape=(input.num_books))
    output_libs = []

    while len(libs) > 0:
        libs = sort_libs(libs, input, isVisited, day)
        l = libs[0]
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
        if day >= input.num_days:
            break
        del libs[0]
    
    out(output_libs)
 
if __name__== "__main__":
    main()
