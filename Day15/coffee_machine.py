import logo
import menu


def payment():
    twenty = int(input("How Many 20 INR Notes: "))
    ten = int(input("How Many 10 INR Notes: "))
    five = int(input("How Many 5 INR Notes: "))
    fifty = int(input("How Many 50 INR Notes: "))
    Hundred = int(input("How Many 100 INR Notes: "))
    total = (twenty * 20) + (ten * 10) + (five * 5) + (fifty * 50) + (Hundred * 100)
    print(total)
    return total

exit_flag = False
print(logo.logo)

while not exit_flag:
    print("We have Espresso. Latte, Cappuccino \n")
    user_input = input("What You Would like to have?\n").lower()
    if user_input == "cappuccino" :
        if menu.machine_stock["water"] >= 250 and menu.machine_stock["milk"] >= 100 and  menu.machine_stock["coffee"] >= 24:
            payment_amt =  payment()
            if menu.cappuccino["cost"] <= payment_amt :
                print("Here is Your Coffee ☕ ! Enjoy")
                menu.machine_stock["water"] -= 250
                menu.machine_stock["milk"] -= 100
                menu.machine_stock["coffee"] -= 24
                print("Change Amount: " + str(payment_amt - menu.cappuccino["cost"]))
            else:
                print("Insufficient Amount, Please Change Amount")
        else :
            print("Sorry 😔 ! We Can't Process Your cappuccino. We are running Out of Stock")
    if user_input == "espresso":
        if menu.machine_stock["water"] >= 50 and menu.machine_stock["milk"] >= 0 and menu.machine_stock["coffee"] >= 18 :
            payment_amt =  payment()
            if menu.espresso["cost"] <= payment_amt :
                print("Here is Your Espresso ☕! Enjoy")
                menu.machine_stock["water"] -= 50
                menu.machine_stock["milk"] -= 0
                menu.machine_stock["coffee"] -= 18
                print("Change Amount: " + str(payment_amt - menu.espresso["cost"]))
            else:
                 print("Insufficient Amount, Please Change Amount")
        else :
            print("Sorry 😔 ! We Can't Process Your Espresso. We are running Out of Stock")
    if user_input == "latte":
        if menu.machine_stock["water"] >= 200 and menu.machine_stock["milk"] >= 150 and menu.machine_stock["coffee"] >= 24 :
            payment_amt =  payment()
            if menu.latte["cost"] <= payment_amt :
                print("Here is Your Latte ☕! Enjoy")
                menu.machine_stock["water"] -= 200
                menu.machine_stock["milk"] -= 150
                menu.machine_stock["coffee"] -= 24
                print("Change Amount: " + str(payment_amt - menu.latte["cost"]))
            else:
                 print("Insufficient Amount, Please Change Amount")
        else :
            print("Sorry 😔 ! We Can't Process Your Latte. We are running Out of Stock")


    if user_input == "report":
        print("Machine Stock Report:")
        print(f"Water: {menu.machine_stock['water']}ml")
        print(f"Milk: {menu.machine_stock['milk']}ml")
        print(f"Coffee: {menu.machine_stock['coffee']}g")
    if user_input == "exit":
        print("Goodbye!")
        exit_flag = True
        exit()


