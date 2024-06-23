city = ["Bengaluru", "Kolkata", "New Delhi", "Mumbai", "Chennai", "Noida", "Gauhwati"]

print(f"Initial List {city}")

#Append (Adding new Item in the List) 
city.append("Agartala")
print(f"City List after append {city}")

#Alter ("Update a Exsiting data")
city[6] = "Guahwati"
print(f"City List after Alter {city}")

#Expand the list (We want to add list items)
city.extend(["Nagpur","Surat","Chandigarh","Imphal"])
print(f"City List after Extend {city}")


#Might As in Interview
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
# First [1] --> vegetables and [1] --> In vegetables Index 1
print(dirty_dozen[1][1])  
