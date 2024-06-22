print("Welcome! to Tip Calculator");
print("12% tip");
total_bill =int(input("Enter total bill\n $"))
guest=int(input("Enter total Number of Guest\n"))

billtip = (total_bill+(total_bill*0.12))/guest

billtip_round = round(total_bill,2)

print(f"Your total amount : ${billtip_round}")
