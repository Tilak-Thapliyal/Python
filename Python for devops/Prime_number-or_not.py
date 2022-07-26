def prime_num_check(n):
    if n > 1:
        for i in range(2, n):
            if n%i == 0:
                print(f"{n}, is not a prime number!")
                break
        else:
            print(f"{n}, is a prime number!")
            
    else:
        print("Enter a valid number!")

prime_num_check(int(input("Enter a num: ")))