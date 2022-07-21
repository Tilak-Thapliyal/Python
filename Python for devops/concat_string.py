def concat_string(n):
    series = ""
    for i in range (1, n+1):
        series += str(i)
    print(f"the series is {series}")

concat_string(int(input("Enter any digit: ")))

