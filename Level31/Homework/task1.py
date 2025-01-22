def greet():
    return "hello world!"

def opposite(number):
    return number * -1

def make_negative( number ):
    if number > 0:
        return number * -1
    else:
        return number * 1
    

def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total


def repeat_str(repeat, string):
    return repeat * string


def square_sum(numbers):
    return sum(num ** 2 for num in numbers)


def find_smallest_int(arr):
    num = min(arr)
    return num


def summation(num):
    return num * (num + 1) // 2


def no_space(x):
    NO_SPACE = x.replace(" " , "")
    return NO_SPACE


def count_sheeps(sheep):
    return sheep.count(True)

