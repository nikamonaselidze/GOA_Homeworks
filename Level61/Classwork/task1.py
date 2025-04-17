def get_average(marks):
    return sum(marks) // len(marks)

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])

def generate_shape(n: int) -> str:
    return '\n'.join(['+' * n] * n)

def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum


def find_it(seq):
    nums = set()
    for num in seq:
        if num in nums:
            nums.remove(num)
        else:
            nums.add(num)
    return nums.pop()