#!/usr/bin/python3
def no_c(my_string):
    aux_c = ''
    for i in my_string:
        if i == 'c' and i == 'C':
            aux_c += 1
        return (aux_c)
