height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI_Calculator = round(weight / height ** 2)

if BMI_Calculator >= 18.5:
    if BMI_Calculator < 25:
        print(f"Your BMI is {BMI_Calculator}, you have a normal weight.")
    elif BMI_Calculator < 30:
        print(f"Your BMI is {BMI_Calculator}, you are slightly overweight.")
    elif BMI_Calculator < 35:
        print(f"Your BMI is {BMI_Calculator}, you are obese.")

else:
    print(f"Your BMI is {BMI_Calculator}, you are underweight.")