#1)შექმენით ფუნქცია რომელსაც გადაეცემა სია,გამოითვალეთ რიცხვების ჯამი for ციკლის საშუალებითაც და sum() ფუნქციის გამოყენებითაც აუცილებლად დააბრუნეთ შედეგი return ის გამოყენებით.

def sum(num1,num2):
    return num1 + num2
print(sum(10,50))

#For ციკლი
def sum(number):
    sum = 0
    for i in number:
        sum += i
    return sum

print(sum(10,50,20))
    