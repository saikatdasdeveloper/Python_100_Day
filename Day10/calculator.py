logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

should_continue = False

while not should_continue:
    first_number = int(input("Enter a number: \n"))
    Operation = input("+ \n- \n/ \nx \n Selected Operation:")
    second_number = int(input("Enter second number: \n"))
    if Operation == "+":
        print(f"Result of Addition: {addition(first_number, second_number)}")

    elif Operation == "-":
        print(f"Result of Subtraction: {subtraction(first_number, second_number)}")

    elif Operation == "x":
        print(f"Result of Multiplication: {multiplication(first_number, second_number)}")

    elif Operation == "/":
        print(f"Result of Division: {division(first_number, second_number)}")
    
    continue_in = input("Do You Want to Continue the Calculator Type Yes or No \n")
    if continue_in.lower() == "no":
        should_continue = True
    if continue_in.lower() == "yes":
        should_continue = False



