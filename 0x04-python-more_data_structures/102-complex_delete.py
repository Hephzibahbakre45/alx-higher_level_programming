#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    val = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            val.append(i)
    for i in val:
        del a_dictionary[i]
    return a_dictionary
