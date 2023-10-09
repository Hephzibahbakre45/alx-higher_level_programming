#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    aux_list = []

    for i in my_list:
        if i % 2 == 0:
            aux_list.append(True)
        else:
            aux_list.append(False)
    return (aux_list)
