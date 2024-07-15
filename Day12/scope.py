##SCOPE

##Global Scope

player_health = 40

##Local Scope
def drink():
    player_health = 10
    print(f"Player Health: {player_health}")


## Calling Both

drink()
print(f"Player Health: {player_health}")

# ##OutPut
# Player Health: 10
# Player Health: 40

##Modifying a Global Scope / Variable Inside a local Scope

player_food = 20

def player_food_level ():
    global player_food
    player_food = 60

##Calling

print(f"Player Food Level : {player_food}")
player_food_level ()
print(f"Player Food Level : {player_food}")

# ##Output
# Player Food Level : 20
# Player Food Level : 60

##Global Constraints

URL= "https://www.google.com"
URL_MY_PORTFOLIO = "http://saikardeveloper.in"
PI = 3.1459

