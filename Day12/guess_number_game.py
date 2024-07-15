import random

print("Welcome to Number Guess Game! 1 to 100")
game_difficulty = input("Enter the game difficulty, Type 'Easy' or 'Hard' \n ====>")

max_number_play = 0

if game_difficulty.lower() == "easy":
    max_number_play = 10
if game_difficulty.lower() == "hard":
    max_number_play = 5


number_guess = random.randint(1,100)

Over = False
while not Over:
    user_guess = int(input("Guess the number: \n ====>"))
    if user_guess == number_guess:
        print("Congratulations, You Win!")
        Over = True
    elif user_guess < number_guess:
        print("Too Low")
        max_number_play -=1
        print(f"Lives : {max_number_play} ")
    elif user_guess > number_guess:
        print("Too High")
        max_number_play -=1 
        print(f"Lives : {max_number_play} ")     

    if max_number_play == 0:
         Over=True
         print("You Lost")

