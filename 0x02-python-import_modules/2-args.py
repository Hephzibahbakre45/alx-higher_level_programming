#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if (len(sys.argv)) == 0:
        print("0 argument:")
    elif (len(sys.argv)) == 1:
        print("1 argument:")
    else:
        (print("{} arguments:".format(len(sys.argv) - 1)))
    for i in sys.argv:
        if (sys.argv).index(i) == 0:
            print("{}: {}".format((sys.argv).index(i), i))
