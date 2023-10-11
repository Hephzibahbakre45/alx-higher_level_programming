#!/usr/bin/python3

def search_replace(my_list, search, replace):
    aux_list = my_list.copy()
    i = 0
    while i < len(aux_list):
        if aux_list[1] == search:
            aux_list[1] = replace
        i += 1
    return (aux_list)
