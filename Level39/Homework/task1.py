def bool_to_word(boolean):
    if boolean == True:
        return("Yes")
    else:
        return("No")
    

def remove_char(s):
    return s[1 : -1]


def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8


def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'


def DNAtoRNA(dna):
    return dna.replace('T', 'U')

