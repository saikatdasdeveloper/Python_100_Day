## Return in Function


# def format__name(f_name, l_name):
#     name = f_name.title() + ' ' + l_name.title()
#     return print(name)

# format__name("saikat","das")


def format__name_type(f_name, l_name):
    if f_name == "" and l_name == "":
        return print("Error: Both First Name and Last Name cannot be empty.")
    name = f_name.title() + ' ' + l_name.title()
    return print(name)

format__name_type(input("Enter Your First Name \n"), input("Enter Your Last Name \n"))