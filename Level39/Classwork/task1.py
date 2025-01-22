def generate_range(start, stop, step):
    num=[]
    for i in range(min,max + 1,step):
        num.append(i)
        return num



def reverse_it(data):
    if type(data) == str or type(data) == int:
        return str(data)[::-1]
    return data


def sum_array(arr):
    if len(arr) <= 2:
        return 0
    arr.sort()
    total_sum = sum(arr) - arr[0] - arr[-1]
    return total_sum


def count_by(x, n):
    return [i * x for i in range(1, n + 1)]