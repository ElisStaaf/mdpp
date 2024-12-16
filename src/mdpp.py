#!/bin/python3

from proc import MDPP
from sys import argv

def main() -> None:
    argc = len(argv)
    if argc != 2:
        print("Insufficient arguments.")
        return
    mdpp = MDPP(argv[1])
    mdpp.evalexpr()
    print(mdpp.out)

if __name__ == "__main__":
    main()
