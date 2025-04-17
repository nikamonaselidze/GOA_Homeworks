def expression_matter(a, b, c):
    cases = [a + b + c]
    cases.append(a * b * c)
    cases.append((a * b) + c)
    cases.append((a + b) * c)
    cases.append(a + (b * c))
    cases.append(a * (b + c))
    return max(cases)



def dup(arry):
    array_new = []
    for string in arry:
        string_new = ""
        prev = None
        for char in string:
            if char != prev:
                string_new += char
            prev = char
        array_new.append(string_new)
        
    return array_new
        


def solve(s):
    upper = 0
    lower = 0
    
    for char in s:
        if char.islower():
            lower += 1
        else:
            upper += 1
            
    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()
    

def max_multiple(divisor, bound):
    return bound - (bound % divisor)


def alphabetic(s):
    return sorted(s) == list(s)