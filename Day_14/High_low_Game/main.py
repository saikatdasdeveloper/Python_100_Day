import random as rand
from game_data import data;
import logo

print(logo.logo)

acc_a = ""
acc_b= ""
game_flag = False
def generate_random() :
    global acc_a, acc_b
    acc_a = rand.choice(data)
    acc_b = rand.choice(data)
    while acc_a == acc_b:
        acc_b = rand.choice(data)

def play():
    score = 0
    generate_random()
    global game_flag
    print(f"Compare A: {acc_a['name']}, A {acc_a['description']}, From {acc_a['country']}")
    print(logo.vs)
    print(f"Compare B: {acc_b['name']}, A {acc_b['description']}, From {acc_b['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if (user_choice == "A") :
        if int(acc_a['follower_count']) > int(acc_b['follower_count']) :
            print("You are Correct!")
            score=score+1
        else:
            print("Sorry! you are Wrong")
            game_flag = True
    elif(user_choice == "B") :
        if int(acc_b['follower_count']) > int(acc_a['follower_count']) :
            print("You are Correct!")
            score=score+1
        else:
            print("Sorry! you are Wrong")
            game_flag = True
    print(f"Your Score: {score}")




while not game_flag:
    play()
