# students_height = input("Input a list of student Heights ").split()
# for n in range(0, len(students_height)):
#     students_height[n] = int(students_height[n])
# # print(students_height)

# total_height = 0
# for height in  students_height:
#     total_height += height
# print(total_height)

# total = 0
# for student in students_height:
#     total += 1
# print(total)

# print(f"average height is {total_height / total}")

# students_scores = input("Input a list of student scores ").split()
# for n in range(0, len(students_scores)):
#     students_scores[n] = int(students_scores[n])
# # print(students_scores)

# first_number = 0
# for i in range(2, 101, 2):
#     first_number += i
# print(first_number)

for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)