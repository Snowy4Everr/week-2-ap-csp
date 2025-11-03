# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Nick"
age = 17
favorite_color = "Blue"
favorite_number = 9

#  Step 2: Practice String Operations
# 1. Print your name in uppercase
print(first_name.upper)

# 2. Print how many letters are in your name
print(len(first_name))

# 3. Combine your name and favorite color into one message
print(f"My name is{first_name}, and my favorite color is{favorite_color}.")
#f"{name}"
#  Step 3: Math Practice
# Use arithmetic operators with your favorite number
num1 = 3
num2 = 3
num3 = int(input("what is your 3rd fav"))
num4 = int(input("what is your 4th fav"))
print(num1 + num2)
print(num3 + num4)

#  Step 4: User Input Practice
# Ask the user two questions and combine answers
ans1 = input("How are you?")
ans2 = input("How many siblings do you have?")
print("You had a " + ans1 + "day, and you have" + ans2 + "sibling(s)." )


# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together
first_name1 = "Nick"
age = 17
year = 1
fav_number = 9
print(f"Hi! My name is {first_name1}. I am {age} years old, and my favorite number is {fav_number}.")
new_age = age + year
print(f"In a year, I will be {new_age} years old.")