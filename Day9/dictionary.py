python_dict = {
    "python" : "python is a advance Programming language",
    "version" : "python 3.9",
    "features" : "high-level, object-oriented, interpreted,dynamic,general-purpose",
    "author" : "Guido van Rossum",
    "year" : "1991",
    "license" : "Python Software Foundation"
}

# Accessing values using keys

# print(python_dict["python"])
# print(python_dict["version"])
# print(python_dict["features"])
# print(python_dict["author"])
# print(python_dict["year"])

# Adding new Item in the dictionary

python_dict["difficulty"] = "easy"
print(python_dict)

# Updating/Editing value of existing item

python_dict["version"] = "python 3.10"
print(python_dict)

# Deleting an item

# del python_dict["license"]
# print(python_dict)

# Checking if a key exists in the dictionary

# if "difficulty" in python_dict:
#     print("Key 'difficulty' exists in the dictionary")
# else:
#     print("Key 'difficulty' does not exist in the dictionary")

# Iterating over dictionary items

for key, value in python_dict.items():
    print(f"Key: {key}, Value: {value}")


# Wiped out of python_dict

# python_dict.clear()
# print(python_dict)

# Or 

# python_dict ={}
# print(python_dict)

#Looping through dictionary items

for key in python_dict:
    print(key)
    print(python_dict[key])