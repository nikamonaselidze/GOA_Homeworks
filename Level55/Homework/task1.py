my_dict = {
    "name": "Nika",
    "age": 25,
    "country": "Georgia"
}

keys_list = []
values_list = []

for key in my_dict:
    keys_list.append(key)
    values_list.append(my_dict[key])

print("Keys:", keys_list)
print("Values:", values_list)