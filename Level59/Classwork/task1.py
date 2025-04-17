def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]


def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
    

def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product


def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])