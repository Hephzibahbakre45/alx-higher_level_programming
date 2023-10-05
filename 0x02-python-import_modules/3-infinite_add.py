#!/usr/bin/python3
import sys
if __name__ == "__main__":
    addition = 0
    for i in sys.argv:
        if (sys.argv).index(i) == 0:
            pass
        else:
            addition += int(i)
    print("{}".format(addition))
