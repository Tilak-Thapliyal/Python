import random
names_string = input("please provide me names: ")
names = names_string.split(", ")
length = len(names)
random_choice = random.randint(0, length - 1)
victim = names[random_choice]
print(victim)