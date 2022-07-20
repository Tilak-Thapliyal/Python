def reverse_string(string):
    new_string = ""
    for i in string:
        new_string = i + new_string
    print(new_string)

reverse_string(input("Please enter your string: "))

