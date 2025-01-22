def solution(string):
    reversed_string = string[::-1]
    return reversed_string

def string_to_number(s):
    return int(s)

def boolean_to_string(b):
    return str(b)

def make_upper_case(s):
    return s.upper()

def bool_to_word(boolean):
    if boolean == True:
        return("Yes")
    else:
        return("No")