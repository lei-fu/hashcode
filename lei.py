import numpy as np
import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        content = [line.strip() for line in lines] 
        for s in content:
            print(s)