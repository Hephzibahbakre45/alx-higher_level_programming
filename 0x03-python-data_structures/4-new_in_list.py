#!/usr/bin/python3

def aux_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return (my_list)
        else:
            my_list[idx] = element
            return (aux_list)
