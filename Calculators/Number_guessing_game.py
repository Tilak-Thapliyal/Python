import random

easy_turns = 10
hard_turn = 5

def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print("you won!")


def difficulty():
    level = input("Choose a difficulty: Type 'easy' or 'hard': ").lower() 
    if level == "easy":
        return easy_turns
    else:
        return hard_turn

def game():

    print("welcome to the guessing game!")
    print("I am thinking of a number between 1 and 100")

    answer = random.randint(1,100)
    print(f"correct answer is {answer}")

    turns = difficulty()
    
    guess = 0
    while guess != answer:
        print(f"you have {turns} chances")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("you lost")
            return
game()
# guess = int(input("Make a guess: "))

# difficulty_choice = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()

# game_over = False

# if difficulty_choice == "easy":
#     attempts = 6
#     print("I am thinking of a number between 1 and 30\nYou have 6 attempts to guess the number.")
#     while not game_over:
#         user_number = int(input("Make a guess: "))
#         if user_number != computer_number:
#             attempts -= 1
#             print(f"you have {attempts} lives")
#         elif user_number == "computer_number":
#             game_over = True
#             print("you won!")
            
        




# elif difficulty_choice == "hard":
#     chances = 3
#     print("I am thinking of a number between 1 and 30\nYou have 3 attempts to guess the number.")


# Game_over = False

# while not Game_over:
#     chance = 3
#     answer = int(input("Make a guess: "))
#     if chance != 0 and answer == random_number:
#         Game_over = True
#         print("you guessed the right number, you won!")
#     elif chance >= 1 and chance != random_number:
#         chance -= 1
#         print(f"you are wrong, you have {chance} left")
#     else:
#         print("you lose")


