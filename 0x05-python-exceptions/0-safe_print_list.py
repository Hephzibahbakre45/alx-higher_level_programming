#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    numb = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")

        except IndexError:
            break
        else:
            numb += 1

    print()
    return (numb)
