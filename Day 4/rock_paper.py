import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_in=input("Enter 0 for rock, 1 for paper, 2 for Scissors")

random_computer_in = random.randint(0,2)

if user_in == "0" :
    print(rock)
if user_in == "1" :
    print(paper)
if user_in == "2" :
    print(scissors)

if random_computer_in == 0 :
    print(rock)
if random_computer_in == 1 :
    print(paper)
if random_computer_in == 2 :
    print(scissors)

if user_in == "0" and random_computer_in == 0 :
    print("Draw")

if user_in == "0" and random_computer_in == 1 :
    print("You Lose")

if user_in == "0" and random_computer_in == 2 :
    print("You Win")

if user_in == "1" and random_computer_in == 0 :
    print("You Win")

if user_in == "1" and random_computer_in == 1 :
    print("Draw")

if user_in == "1" and random_computer_in == 2 :
    print("You Lose")

if user_in == "2" and random_computer_in == 0 :
    print("You Lose")

if user_in == "2" and random_computer_in == 1 :
    print("You Win")

if user_in == "2" and random_computer_in == 2 :
    print("Draw")

