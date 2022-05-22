print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?(please don't add %) "))
people = int(input("How many people to split the bill? "))

#total bill including tip
total_bill = bill + bill * (tip/100)

#per person has to pay and round off
bill_per_person = total_bill / people
final_format = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_format}")
