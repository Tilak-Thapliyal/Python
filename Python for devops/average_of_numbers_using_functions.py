
def number_collector(total_number):
    for i in range (total_number):
        input_1 = input("enter numbers: ")
        list.append(input_1)



def average_calculator():
    total_sum = 0
    for element in range(len(list)):
        total_sum = total_sum + float(list[element])
    print(f"the average is: {(total_sum/len(list))}") 

list = []

number_collector(int(input("average of how many number?: ")))

average_calculator()



# def collectNumbers(totalNumbers):
#         print("Please enter", totalNumbers, "numbers:")
#         for i in range(0,totalNumbers):
#             ele = float(input())
#             myList.append(ele)

# # Calculates average  

# def calculateAverage():
#     total = 0
#     for i in range(0,len(myList)):
#         total = total + myList[i]
#     return (total/totalNumbers) 

# myList = []

# totalNumbers=int(input("Average of how many numbers? "))
# collectNumbers(totalNumbers) # Calling function to create a list

# average=calculateAverage()  # Calling function to calculate average
# print("The average is : ", average)