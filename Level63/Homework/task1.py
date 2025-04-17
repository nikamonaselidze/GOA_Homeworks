def is_isogram(string):
    return len(string) == len(set(string.lower()))


def to_jaden_case(string):
    if len(string) == 0:
        return string
    
    str = string.split()
    for i in range(len(str)):
        str[i] = str[i].capitalize()

    return ' '.join(str)


def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]


def row_sum_odd_numbers(n):
    return sum(range(n*(n-1)+1, n*(n+1), 2))