# Sum of a sequence
def sequence_sum(begin, end, step):
    last = 0
    for i in range(begin,end+1,step):
        last += i
    return last

# Regex count lowercase letters
def lowercase_count(strng):
    last = 0
    for i in strng:
        if i.islower():
            last += 1
    return last

 
# Small enough? - Beginner
def small_enough(array, limit):
    for num in array:
        if num > limit:
            return False
    return True

# Miles per gallon to kilometers per liter
def converter(mpg):
    kpl = (mpg * 1.609344) / 4.54609188
    return round(kpl, 2)
