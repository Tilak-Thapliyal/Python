def prime_or_not(n1, n2):
    if n1 == 1 or n1 > n2 or n1 == n2:
        print("Enter a valid numbers!")
    elif n1 > 1 and n2 > 2 and n1 < n2:
        for i in range(n1, n2+1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(f"{i}, is a prime number")
    else:
        print("Enter a valid numbers!")

prime_or_not(int(input("Enter first number: "), int(input("Enter second number: "))))


