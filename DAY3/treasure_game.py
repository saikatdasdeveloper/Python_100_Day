print(
     '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************   ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path=input("Where You want to go? Type right or left \n -->").lower()

if path == "left":
    cross = input("You are in a lake. There is an island in the middle of the lake. Type Swim for Swimming to the Island or Wait for Boat \n -->")
    if cross == "swim":
        print("Game Over")
    if cross == "wait":
        print("You are in Island and You have 3 Houses infront of You: Red, Blue and Yellow")
        house = input("Which House You want to go? Type Red, Blue or Yellow \n -->").lower()
        if house == "red":
            print("Game Over. You are in house of fire")
        if house == "blue":
            print("Game Over. You are in house of water")
        if house == "yellow":
            print("Congratulations! You have won!")
else:
    print("GAME OVER")