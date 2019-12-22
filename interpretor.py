import os
import parsor

if __name__ == "__main__":


    w = []
    l = []
    i = []

    w, l, i = parsor.parse_main_functionality("tests/aliens")

    print(w)
    print(l)
    print(i)
