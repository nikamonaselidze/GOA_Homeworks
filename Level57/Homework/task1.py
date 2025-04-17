def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]


def count_by(x, n):
    arr = []
    for num in range(1, n+1):
        result = x * num
        arr.append(result)
    return arr


def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


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