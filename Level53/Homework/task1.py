my_set = {10, 20, 30, 40}

try:
    print(my_set[0])
except TypeError as e:
    print("ინდექსით წვდომა შეუძლებელია:", e)

try:
    my_set[0] = 99
except TypeError as e:
    print("ელემენტის შეცვლა ინდექსით შეუძლებელია:", e)




# 1. list-ში ელემენტები შეიძლება განმეორდეს, ხოლო set-ში – არა.
# 2. list-ში ელემენტები დალაგებულია (ordered), ხოლო set-ში – არადალაგებული (unordered).
# 3. list-ში შესაძლებელია ინდექსზე წვდომა (indexing), set-ში – არა.
# 4. list გამოყენებულია როდესაც ელემენტების თანმიმდევრობა მნიშვნელოვანია.
# 5. set გამოიყენება დუბლიკატების მოსაშორებლად და სწრაფი საძიებლად.




food_set = {"Burger", "Pizza", "Fries", "Hotdog"}

food_set.clear()

healthy_food = {"Avocado", "Salad", "Apple", "Oats"}

food_set.update(healthy_food)




print("ახალი სეტია:", food_set)


def remove_duplicates(input_list):
    return list(set(input_list))

list1 = [7, 5, 44, 14, 5, 5, 44]
list2 = [89, 90, 56, 45, 90, 78, 90]

print("List1 უნიკალური:", remove_duplicates(list1))
print("List2 უნიკალური:", remove_duplicates(list2))