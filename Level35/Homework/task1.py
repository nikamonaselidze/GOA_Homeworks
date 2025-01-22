def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())



def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))


def lowercase_count(strng):
    return sum(a.islower() for a in strng)


def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)


def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product


def smash(words):
    return " ".join(words)


