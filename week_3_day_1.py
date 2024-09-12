# # Week3
# # This week we will work on :
# # Working With Strings


# # 1.   Working With Numbers
# # 2.   Getting Input From Users




# # 1.   Building a Basic Calculator
# # 2.   Mad Libs Game




































# # # Review
# # create variables for the following :
# # 1. age
# age = 17 #interger 
# # 2. name
# name = "yao"
# # 3. song
# song = "annie. - Wave to Earth,"
# # 4. food
# food = "barria "
# # 5. number
# number = 100


# # #now include the variables you just made print in the following...


# # Once upon a time, there was a [age] old coder named [name].
# print("Once upon a time, there was a " ,age, 
#        "old coder named", name)


# # [name] liked to hum the song [song] while coding. It was so annoying that their teammates would throw [food] until [name] would stop singing.
# print(name, "liked to hum the song ", song, 
#       "while coding . It was so annoying that their teammates would throw", food, 
#        "until", name, "would stop singing." )

# # Still, [name] was the best coder on the team and could write [number] lines of code every day. Maybe [song] was [name]’s secret power?
# print("Still", name, "was the best coder on the team and could write",
#       number, "lines of code every day. Maybe", song, "was", name,
#       "'s secret power?"  )


# number1="$100"
# number2="$200"
# number3="$300"
# number4="$400"
# number5="$500"


# print (number1 
# ,number2 
# ,number3
# ,number4
# ,number5, "that how much money I have"
# )












##########################################################################################
# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
#    or 'I' (uppercase letter eye) as single character variable names.
# 6. Avoid using words that have special meaning in Python like "list" and "str"


# Here are some exercises to practice the rules:


# Correcting Invalid Names: Below are some invalid names. Correct them according to the rules:


# first_name
# last_name
# email_address
# percent
# variable_name
# O
# list
# Creating Valid Names: Create valid names for the following descriptions:


# The first name of a person
# The last name of a person
# The email address of a person
# The percentage of marks obtained by a student
# A variable to store the number of items in a shopping cart




# Identify Valid and Invalid Names: Identify which of the following names are valid or invalid according to the rules:


# first_name
# lastName
# email_address
# percentage
# variable_name
# first_variable
# email_address
# percentage
# i
















############################################################################################


# # **Working with** **numbers** **bold text**
# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers.
# Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.


##########################################################################################
# #addition
print(2+1)
# #multiplication
print(2*2)
# #division
print(3/2)
# #modulo
print(3%2)
# #powers
print(2**3)
# #get the max and min of a number
print(max(1,2)) # max number get the largest number 
print(min(1,2)) # min number get the smallest number 
# #round a number
print(round(3.4))
# # absolute value
print(abs(-3)) # the distance between the value to zero, always positive 
# # order of operations
print(2+10/3*5)
# #to do more you need to import special math libraries from python
from math import *    
# #this goes out and grabs some different math functions we can use
# #floor method
print(floor(3.7))
# #ceil method
print(ceil(2.7))
# #sqrt method
print(sqrt(36))














##########################################################################################
# So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
# # **Getting Input from users**
# #how do we get input from users?
# input("what is your name?")
name = input("Whats your name?")
print("Hello", name)
# # basic math calculator
# #ask the user for 2 numbers
num1 = input("enter a number")
num2 = input("enter another number")
# # print out a statement where you:
# # add them together
print(num1 + num2)
# #multiply
print(num1*num2)
# # find the max number
print(max(num1,num2))
# # find the remainder of the numbers
print(num1%num2)
# #round one number
print(round(num1))








##########################################################################################
# # mad libs game
# print("Roses are {color}")
# print("{plural noun} are blue")
# print("I love {celebrity}")
# # On to codehs.com







