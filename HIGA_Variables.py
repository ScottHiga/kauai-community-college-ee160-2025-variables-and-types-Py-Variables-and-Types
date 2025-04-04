################################################
#HIGA_Variables.py demonstrates how to set strings as variables and how to use operations to add multiple string variables
#Created On: March 02, 2025
#Last Edited: April 03, 2025
################################################


ten_thousand = 10000
# setting variable 'ten_thousand' to value 10000

three = 3
# setting variable 'three' to value 3

zero = 0
# setting variable 'zero' to value 0

print (ten_thousand/three)
print (type(ten_thousand/three))
# printing the quotient of variables ten_thousand and three.  This will give us a decimal because Python will default to a float if nothing else is specified?

print (int(ten_thousand/three))
# This is asking python to print the quotient of variables ten_thousand and three as an integer.  Since 333.333... is not a whole number, Python will round to the nearest integer for us.

print (ten_thousand + three)
# printing the sum of variables ten_thousand and three.

print (three*zero)
# printing the product of variables three and zero.

# print (ten_thousand/zero)
# If we try to divide by zero, we get the error 'division by zero.'  As in math, we cannot divide by zero in Python

yah = "hello"
# setting variable 'yah' to the string "hello"

yeet = "world"
# setting variable 'yeet' to the string "world"

space = " "
# setting the variable 'space' to the string " "

exclamation_point = "!"
# setting the variable 'exclamation_point' to "!"

print (type(yah+space+yeet+exclamation_point))
print (yah+space+yeet+exclamation_point)
# printing the sum of the four varaibles as a string.

# print (yah-yeet)
# If we try to use any other operation besides addition with variables that are strings then we get the error 'unsupported operand type(s) for '.  We can only use the addition operator (+) to manipulate strings

print (type(three))
# printing the type of the variable three. It's an int at this point of the script

three = float(3)
# setting an integer value to a float

print(type(three))
# printing the type of the variable three after we reassigned it to be a float.  It's a float at this point of the script

# print (float(yah))
# We can't change this particular string to a float because the string variable is made up of text and text cannot be converted to a decimal value.

print("")
print("Done!")