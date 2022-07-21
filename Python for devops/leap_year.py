def leap_year(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 == 0:
            print("it's a leap year!")
        else:
            print("it's not a leap year!")
    else:
        print("it's not a lep year!")

leap_year(int(input("emter a year in numbers: ")))