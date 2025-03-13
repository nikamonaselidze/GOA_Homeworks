# Take a Ten Minutes Walk
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    x, y = 0, 0
    
    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
    
    return x == 0 and y == 0

# The @ operator

def evaluate(expr):
    if ' @ ' in expr:
        tokens = expr.split(' @ ')
    else:
        tokens = expr.split('@')

    tokens = list(map(int, tokens))
    
    def at_operator(a, b):
        if b == 0:
            return None  
        return (a + b) + (a - b) + (a * b) + (a // b)

    result = tokens[0]
    for num in tokens[1:]:
        result = at_operator(result, num)
        if result is None:
            return None