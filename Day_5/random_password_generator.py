import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(0, nr_letters+1):
    random_char = random.choice(letters)
    password += random_char

# print("Password: " + password)

sym_pass = ""
for char_sym in range(0, nr_symbols+1):
    random_char_sym = random.choice(symbols)
    sym_pass += random_char_sym

# print("Password: " + sym_pass)

num_pass =""
for char_num in range(0, nr_numbers+1):
    random_char_num = random.choice(numbers)
    num_pass += random_char_num

# print("Password: " + num_pass)

print("Your Password: " + password + sym_pass + num_pass)