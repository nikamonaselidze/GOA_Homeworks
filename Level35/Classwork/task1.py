def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    return uppers


def max_multiple(divisor, bound):
    return bound // divisor * divisor


def sumDigits(number):
    number = abs(number)
    return_number = 0
    
    while number > 0:
        return_number += number % 10
        number = int(number / 10)
        
    return return_number


def dont_give_me_five(start,end):
    return len([num for num in range(start, end+1) if '5' not in str(num)])