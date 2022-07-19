index = int(input("Enter the index till you want series: "))

first_number = 0
second_number = 1
temp = 0

print(first_number)
print(second_number)

for i in range(0, index):
    temp = first_number + second_number
    first_number = second_number
    second_number = temp
    print(temp)


