# print("Welcome to the tip calculator")
# total_bill = float(input("what was the total bill? $"))
# number_of_people = int(input("How many people to split the bill? "))
# tip = int(input("What percentage tip you like to give? 10, 12 or 15? "))

# tip_calculator = round((((total_bill * (100 + tip)) / 100) / number_of_people), 2)

# print(f"Each person should pay: ${tip_calculator}")

# print("Welcome to treasure Island!")
# choice_1 = input("Please choose left or right:").lower
# if choice_1 == "right":
#     print("Fall into a hole. Game over!")
# else:
#     choice_2 = input("do you want swim or wait? ").lower
#     if choice_2 != "wait":
#         print("Attacked by trout. Game over!")
#     else:
#         choice_3 = input("which door? ").lower
#         if choice_3 == "red":
#             print("Burned by Fire. Game over!")
#         elif choice_3 == "blue":
#             print("Eaten by beasts. Game over!")
#         elif choice_3 == "yellow":
#             print("You win")
#         else:
#             print("game over!")

# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)'''
# computer_choice = [rock, paper, scissors]

# random_choice = random.choice(computer_choice)     
# print(f"{random_choice}")
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the Password generator!")
# nr_letters = int(input("how many letters would you like in your password?\n "))
# nr_symbols = int(input("how many symbols would you like?\n "))
# nr_numbers = int(input("how many numbers would you like?\n"))

# i = 0
# password = []
# while i < nr_letters: 
#     new_letter = random.choice(letters)
#     password.extend(new_letter)
#     i += 1

# i = 0
# while i < nr_symbols:
#     new_symbol = random.choice(symbols)
#     password.append(new_symbol)
#     i += 1

# i = 0
# while i < nr_numbers:
#     new_number = random.choice(numbers)
#     password.append(new_number)
#     i += 1

# random.shuffle(password)

# final_password = ""
# for element in password:
#     final_password += element

# print(f"your password is {final_password}")






