dictionary = {"kishor":89 , "mahir":78 , "riya" : 85}
name = input("Enter the name to search: ")
if name in dictionary:
    print(dictionary.get(name))
else :
    print("name does not match ")
