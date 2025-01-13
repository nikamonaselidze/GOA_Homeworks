#1)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ კი გამოიტანეთ ამ რიცხვების ჯამი.

numbers=[100 , 15]

def list_numbers():
    for i in numbers:
        numbers += i
        print(numbers)