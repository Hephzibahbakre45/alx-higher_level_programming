#!/usr/bin/python3
for numb in range(100):
    if (numb == 99):
        print("{}".format(numb))
    else:
        print("{:02d}, ".format(numb), end="")
