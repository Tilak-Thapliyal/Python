from posixpath import split


def sum(n):
    split_number = split(n)
    print(split_number)

sum(int(input("enter a num:" )))