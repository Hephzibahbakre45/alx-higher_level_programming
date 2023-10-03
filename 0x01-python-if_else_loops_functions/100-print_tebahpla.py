#!/usr/bin/python3
numb = 122
count = 0
while (count < 26):
    if (count % 2 == 0):
        no = numb
    else:
        no = numb - 32
    print("{}".format(chr(no)), end="")
    numb -= 1
    count += 1
