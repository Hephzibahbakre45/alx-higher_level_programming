#!/usr/bin/python3

def text_indentation(text):
    '''
    indent text
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.split()
    new_row = ""
    for i in text:
        if new_row != "":
            new_row += " "
        if "." in i or "?" in i or ":" in i:
            new_row += i
            print(new_row)
            print()
            new_row = ""
        else:
            new_row += i
    if new_row != "":
        print(new_row)
