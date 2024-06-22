##Nested if/else statements

print("Welcome to Roller Coster");
height = int(input("Enter Your Height in cm\n -->"))
age = int(input("Enter Your Age in\n -->"))
if height >= 120:
    print("You can ride the roller coaster")
    if age >= 45 and age <= 55:
        senior_citizen = True
        bill = 0
        print("You are on Senior Fare: $ 0")
    elif age > 12 and age < 18:
        senior_citizen = False
        bill = 7
        print("You are on Teenage Fare: $ 7")  
    elif age >= 18:
        senior_citizen = False
        bill = 12
        print("Your are on Adult Fare: $ 12")
    else:
        senior_citizen = False
        bill = 5
        print("You are on Child Fare: $ 5")

    want_photo = input("Want a Photo to be Clicked, Type Y for Yes or N for No \n -->")
    if want_photo == "Y" or senior_citizen == True:
        total_bill = 0
        print(f"Your total ticket : $ {total_bill}")
    elif  want_photo == "Y":
        total_bill = bill+3
        print(f"Your total ticket : $ {total_bill}")
    else:
        total_bill = bill
        print(f"Your total ticket : $ {total_bill}")

else:
    print("Sorry you have to grow taller before you can ride")

