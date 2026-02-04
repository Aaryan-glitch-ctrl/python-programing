


number = int(input("Enter a non-negative integer: "))


if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
   
    result = math.factorial(number)
    print(f"The factorial of {number} is {result}")
