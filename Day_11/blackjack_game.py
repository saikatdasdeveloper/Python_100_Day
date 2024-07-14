import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

card_deck = ["Ace",1,2,3,4,5,6,7,8,9,10,"King","Queen","Jack"]
print(len(card_deck))


def gen_random_card():
    random_card = random.choice(card_deck)
    if random_card == "Ace":
          random_card = 1
    elif random_card == "King" or random_card == "Queen" or random_card == "Jack":
          random_card = 10
    return random_card

score_play = []
score_computer = []

game_continue = False
score_play_add = 0
score_comp_add = 0

while not game_continue:
      should_game_continue = input("Do You Want to Continue the Game? (y/n): ").lower()

      if (should_game_continue == "y"):
            print("--------------------------------------")
            score_play.append(gen_random_card())                 
            score_computer.append(gen_random_card())
            print(f"Your Card: {score_play}")
            print(f"Computer Card: {score_computer[0]}")
            print("--------------------------------------")
            for i in range(len(score_play)):
                  score_list =  score_play[i]
            score_play_add = score_play_add + score_list
            print(f"Your Total Score: {score_play_add}")
            for i in range(len(score_computer)):
                  score_list =  score_computer[i]
            score_comp_add = score_comp_add + score_list
            print(f"Computer Total Score: {score_comp_add}")
            print("--------------------------------------")

            if score_play_add > 21 or score_comp_add > 21:
                  if score_play_add > 21:
                        print("Computer Lose!")
                  else:
                        print("You Win")
                  game_continue = True
            

