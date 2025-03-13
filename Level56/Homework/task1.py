# Nickname Generator
def nickname_generator(name):
    if len(name) < 4:
        return  "Error: Name too short"
    
    
    vowels = "aeiou"
    
    
    if name[2].lower() in vowels:
        return name[0:4]
    else:
        return name[0:3]
    

print(50 // 2)