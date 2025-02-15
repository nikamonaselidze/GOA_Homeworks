def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))


def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list



def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


def sum_mix(arr):
    return sum(map(int, arr))


def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)


def reverseWords(str):
    return " ".join(str.split(" ")[::-1])

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))