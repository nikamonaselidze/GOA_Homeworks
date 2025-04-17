user_dict = {}

key = input("შეიყვანე key: ")
value = input("შეიყვანე value: ")

user_dict[key] = value

new_value = input(f"შეცვალე {key}-ის მნიშვნელობა: ")
user_dict[key] = new_value

print("Final dictionary:", user_dict)
