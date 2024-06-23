# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
# print(names)
# 🚨 Remember to remove the print statement above when you submit.
import random
names = ["Saikat","Ankita", "Deep","Shovan","Megha","Goutam","Sorajit","Bishal"]
max_index=len(names)
random_names = random.randint(0,max_index-1)
bill_payer = names[random_names]
print(f"{bill_payer} is going to buy the meal today!")
