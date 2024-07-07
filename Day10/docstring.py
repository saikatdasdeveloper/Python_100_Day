def my_function(f_name,l_name):
    """This function takes first and last name as input and returns the full name in Title Case."""
    name = f_name.title() + " " + l_name.title()
    return name

# Test the function
print(my_function(input("Enter Your first name \n"),input("Enter Your last name \n")))

