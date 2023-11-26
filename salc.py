# A simple calculator program

"""
Author: Kyle Freidhof
Created: November, 25 2023
Program: Simple Calculator Program
About: A program that does simple Mathematical things. Does addition subtraction
Multiplication Division exponents and solves for remainders 
Reason: This was just a project i thought up of for fun. 

"""
# Below are some varriables to hold some text in place

# This varriable is input an asks the user what they want to do 

while True:
    
    inp = input("What do you want to do: ")

    # These are varriables for the if statements below. 
    addition = "Choose the numbers you want to solve for addition"
    subtraction = "Choose the numbers you want to solve for subtraction"
    Multiply = "Choose the numbers you want to solve for multiplication"
    divide = "Choose the numbers you want ti solve for Division"
    expon = "Choose the numbers you want to solve for exponents"
    reman = "Choose the numbers you want to solve for remainders"

    # These are varriables for the input below.
    field1 = "Enter a number: "
    field2 = "Enter another number: "

# Error Message if the user chooses the wrong option
    error_message = "Wrong option"
    # An if statement that says if the input above equals ex 
# Then run the following below 
    if inp == str("ex"):
    # Give the user two input fields
        print(expon)
        i = input(field1)
        y = input(field2)

    # Store the numbers inside the varriables below
        i = int(i)
        y = int(y)

# Then solve exponent by printing out the results 
        print(i ** y)

# This is a elif Statement if the input above equals add 
# Do the following below
    elif inp == str("add"):
    # Give the user two input fields 
        print(addition)
        i = input(field1)
        y = input(field2)

    # Then store the inputs in the varriables here
        i = int(i)
        y = int(y)

# Then solve addition by printing out the results 
        print(i + y)

# if the elif statement is equal sub as above then
# do the following below 
    elif inp == str("sub"):
    # Give the user two input fields 
        print(subtraction)
        i = input(field1)
        y = input(field2)
         # Store the inputs in the varriables 
        i = int(i)
        y = int(y)

    # Then print out the results of the subtraction problem
        print(i - y)

# if the elif statement equals Mult as above then 
# Do the following below
    elif inp == str("Mult"):
    # Give the user two input fields 
        print(Multiply)
        i = input(field1)
        y = input(field2)

    # Then store the inputs in the varriables below 
        i = int(i)
        y = int(y)

    # Then solve the multiplication problem 
        print(i * y)

# if the elif statement equals div then 
# Do the following below  
    elif inp == str("div"):
    # Give the user two input fields 
        print(divide)
        i = input(field1)
        y = input(field2)

    # Then store the inputs in the varriables below
        i = int(i)
        y = int(y)

    # Then solve the divison problem
        print(i / y)
        # if the elif statement equals re
# Do the following below
    elif inp == str("re"):
# Give the user two input fields 
        print(reman)
        i = input(field1)
        y = input(field2)
# Store the inputs in the varriables
        i = int(i)
        y = int(y)

# Then solve the Remainder 
        print(i % y)

# if the user types x then exit the program
# 
    elif inp == str("x"):
        print("Exiting Program")
        break

    elif inp == str("l"):
        print("This gives you a list of options")
        print("add: This will perform addition")
        print("sub: perform subtraction")
        print("Mult: Will perform Multiplication")
        print("div: This will perform multiplication")
        print("ex: This will solve exponents")
        print("re: This will solve remainders")
        print("x: This will exit out of the program.")
        print("l: As you just ran this will list the options you can run")

# If anything else is done print the error message 
    else:
        print(error_message)
        break
