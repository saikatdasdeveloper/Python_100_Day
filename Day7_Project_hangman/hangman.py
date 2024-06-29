import random;
word_list = ["mouse", "button", "india","cricket"];

randomword = random.choice(word_list);

hangman_asci_art = '''88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  
                                    aa,    ,88                                
                                     "Y8bbdP"         '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# print("Random word: " + randomword)

print(hangman_asci_art)
display = []
for _ in range(len(randomword)):
    display += "_"
print(display)


word_len = len(randomword)

## Below block takes that input to the Choosen Word for search that the letter is in that list or not
# for letter in randomword:
#     if letter == in_guess:
#         print("Right")
#     else:
#         print("Wrong")
lives = 6
end_of_game = False
#Main Logic
while not end_of_game:
    in_guess = input("\nENTER A LETTER: ").lower()
    for position in range(word_len):
        letter = randomword[position] 
        if letter == in_guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("Congratulations, You Win!")
    
    if in_guess not in randomword:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose! The word was:", randomword)
