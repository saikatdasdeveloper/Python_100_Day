## Function 

def function():
    print("Hello Function!")


# function()

# Function with Passing arguments/Input
# Parameter is the name of the data.
# While, Argument is the value of the data

def greet(name):
    print("Hello " + name + "!")

# greet("Saikat")

# Function with more than 1 Input/Arg

def fun_more_input(name, location):
    print(f"Hello {name}! You are from {location}.")

# fun_more_input("Saikat", "Bengaluru")

# Function with Keyword arguments/Input
def fun_keyword(name, location,nativeplace):
    print(f"Hello {name}! You are from {location} and your native place is {nativeplace}.")

fun_keyword(location="Bengaluru", nativeplace="Belonia, Tripura", name="Saikat")
