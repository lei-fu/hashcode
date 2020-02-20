import numpy as np
import sys

    

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        content = f.readlines()
        content = [x.strip() for x in content] 
        for s in content:
            print(s)