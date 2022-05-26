print('''  
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  ''')

print('You\'r in "Treaure Island". \nYour mission is to find the Treasure.')
first_question = input("left or right?\n").lower()

if first_question == "left":
    second_question = input("swim or wait?\n").lower()
    if second_question == "wait":
        third_question = input("which door? blue, red or yellow\n").lower()
        if third_question == "yellow":
            print("YOU WIN!")
        elif third_question == "blue":
            print("Eaten by beasts \nGame Over.")
        elif third_question == "red":
            print("Burned by fire. \nGame Over.")
        else:
            print("Game Over.")
    else:
        print("game over!")
    

else:
    print("Fall into a hole.\nGame Over.")

    








