alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

print('''                                                                  
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88     ''')
print('''           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             ''')
def encrypt(input, shift_amount):
    new_word = ""
    for i in range(len(input)):
        letter = input[i]
        if letter ==' ':
         new_word += ' '
        else:
         new_letter_pos = alphabet.index(letter) + shift_amount
         new_letter= alphabet[new_letter_pos]
         new_word += new_letter
    
    print(f"Your Encrypted Text : {new_word}")

def decode(input, shift_amount):
    new_word = ""
    for i in range(len(input)):
        letter = input[i]
        if letter ==' ':
         new_word += ' '
        else:
         new_letter_pos = alphabet.index(letter) - shift_amount
         new_letter= alphabet[new_letter_pos]
         new_word += new_letter
    print(f"Your Decrypted Text : {new_word}")

operation = True
while (operation == True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to decrypt:\n")
    if direction == "encode":
       text = input("Type your message:\n").lower()
       shift = int(input("Type the shift number:\n"))
       encrypt(text,shift)
    elif direction == "decode":
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      decode(text,shift)
    if direction == "exit":
       operation = False
       