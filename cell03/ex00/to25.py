number = int(input("Enter a number less than or equal to 25\n"))

if number > 25:
    print("Error")
else:
    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1