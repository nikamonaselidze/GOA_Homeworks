def string_to_array(s):
    words = []
    word = ""
    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""
    if word:
        words.append(word)
    return words


def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    


def DNAtoRNA(dna):
    return dna.replace('T', 'U')


def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'


def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8


def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0


def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"


def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result


def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4
    
    
def remove_exclamation_marks(s):
    return s.replace('!', '')