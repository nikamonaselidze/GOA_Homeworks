# 1)შექმენით ცარიელი სია და for ციკლის მეშვეობით ჩაამატეთ ყველა ლუწი რიცხვი 0დან 200მდე, ბოლოს დაბეჭდეთ სია.


nums=[]
for i in range(0,200):
    if i % 2 == 0:
        nums.append(i)
        print(nums)


# 2)შექმენით ცარიელი სია და for ციკლის მეშვოებით მომხმარებელს შეეკითხეთ მისი top 5 საყვარელი სახელი (ანუ ხუთჯერ input).

names=[]


for i in range(5):
    names.append(input("Enter your fav name: "))
    print(names)


# 3)შექმენით სია 10 ელემენტით და გამოიტანეთ მხოლოდ კენტ ინდექსზე მდგომი ელემენტები.

element=["nika","Gio","Lasha","Abrama","Noza","Rati","Rezi","Zauri","Mari","Iza"]

for i in element:
    if i % 2 == 1:
        print(element.pop(i))

# 4)შექმენით ცვლადი რომელშიც შენახული იქნება სტრინგი შემდეგ კი გაიგეთ ამ სტრინგის სიმბოლოების რაოდენობა.

string="GIOO"

print(len(string))

# 5)შექმენით სია შემდგარი 5 ელემენტისგან, მომხმარებელს შემოატანინეთ რიცხვი და სიიდან ამოაგდეთ შემოტანილ რიცხვის ინდექსზე მდგომი ელემენტი.

Num1=[1,2,3,4,5,]

user= input("Enter your number: ")
Num1.insert(2,user)
Num1.pop(2)

print(Num1)

# 6)შექმენით სია და დაბეჭდეთ ამ სიის სიგრძე.

List=[4,2,3,45,5,6,2,35,6,6,23,4,234,65,6,24]
len(list)
print(List)