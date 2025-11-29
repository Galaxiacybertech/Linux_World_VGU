try:
    num = float(input("Enter a number: "))

    if num < 0:
        print("The number is negative")
    elif num > 0:
        print("The number is positive")
    else:
        print("The number is zero")

except ValueError:
    print("Please enter a valid numeric value.")