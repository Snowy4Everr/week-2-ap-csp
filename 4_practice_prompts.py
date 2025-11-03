
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it
kb = "keyboard"
m = "mouse"
mp = "mousepad"
print(f"In AP Comp Sci, I use a {m}, {kb}, and {mp}.")

# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.
name = "Nick"
date = "November 3"
movie = "The Godfather"
age = "17"
print(name)
print(date)
print(movie)
# Print your name and age on separate lines using a single print() function.
print(f"Name: {name}\nAge: {age}")
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."

print(f"In 10 years, {name} will be {age + 10} years old.")
##############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
print("Hello World")
name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value


#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen
blue_beetle_summary= "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."
# upper case the entire summary
print("Uppercase:", blue_beetle_summary.upper())
# print the length of the summary
print(len(blue_beetle_summary))
# print the summary
print(blue_beetle_summary)
# print the summary in lowercase
print(blue_beetle_summary.lower())
# replace the word blue with red
BB = blue_beetle_summary.replace("Blue", "Red")
print(BB)
# print the summary
print(blue_beetle_summary)
# string index the word beetle and print it out
print(blue_beetle_summary[-7 : -1])
# print the last word of the summary
print(blue_beetle_summary[-7 : -1])
# print the summary in reverse
print(blue_beetle_summary[: : -1])


##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.

# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
print("You are learning " + input("What are you learning today: "))
# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
print("You are from " + input("Where are you from: "))
# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.
print("Your name is :" + input("What is your name :"))
print("Your surname is :" + input("What is your surname : "))
# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.
print("Your name is:" + input("What is your name : ") + " and your favorite color is :" + input("What is your favorite color"))







