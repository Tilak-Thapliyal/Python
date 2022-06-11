import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

choice_1 = int(input("Please select: 0 for rock, 1 for paper and 2 for scissors\n"))

if choice_1 >= 3 or choice_1 < 0:
    print("you lose!")
else:
    print(game_images[choice_1])

    choice_2 = random.randint(0, 2)
    print(f"computer chose:\n{game_images[choice_2]}")


    if choice_1 == choice_2:
        print("It's a draw!")
    elif choice_1 == 1 and choice_2 == 0:
        print("you win!") 
    elif choice_1 == 0 and choice_2 == 2:
        print("you win!")
    elif choice_1 == 2 and choice_2 == 1:
        print("you win!")
    elif choice_1 == 0 and choice_2 == 1:
        print("you lose!")
    elif choice_1 == 2 and choice_2 == 0:
        print("you lose!")
    elif choice_1 == 1 and choice_2 == 2:
        print("you lose!")

