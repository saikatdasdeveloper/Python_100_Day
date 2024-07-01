##Nesting

#Nesting a list in dictionary

dict_list_nst = {
    "name": "Saikat",
    "College": "Tripura Institute of Technology",
    "Courses": ["Python", "Engineering", "Embeded Systems", "Web Development"]
}

print(dict_list_nst["Courses"])

#Nesting a dictionary in a dictionary

dict_dict_nst = {
    "France" : {"Cities_Visited": ["Paris", "Lille"], "Visted" : 10},
    "India" : {"Cities_Visited": ["Delhi", "Mumbai"], "Visted" : 8}
}

print(dict_dict_nst["France"]["Cities_Visited"])

#Nesting a dictionary in a list

list_dict_nst = [
    {
        "name": "Saikat",
        "age" : "23",
        "location" : "Bengaluru",
        "Visited" : ["Kolkata", "Agartala, Chennai"]
    },
    {
        "name": "Ankita",
        "age" : "21",
        "location" : "Mumbai",
        "visited" : ["Chennai", "Noida"]
    }
]

print(list_dict_nst[0]["location"])




## Example
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])