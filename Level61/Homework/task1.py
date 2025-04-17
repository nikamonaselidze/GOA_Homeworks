def filter_list(l):
  return [i for i in l if isinstance(i, int)]


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


def find_short(s):
    return len(sorted(s.split(), key=len)[0])


def friend(x):
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names


def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))