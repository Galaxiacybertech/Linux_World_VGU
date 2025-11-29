print("~" * 40)
print("       SIMPLE CALCULATOR & CONVERTER       ")
print("~" * 40)
print("""
What do you want to do?
1. Arithmetic Operations
2. Unit Conversions
""")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":

    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        print("""
Choose the operation:
a. Addition
b. Subtraction
c. Multiplication
d. Division
""")

        operation = input("Enter your choice (a/b/c/d): ")

        if operation == "a":
            print("Addition =", num1 + num2)

        elif operation == "b":
            print("Subtraction =", num1 - num2)

        elif operation == "c":
            print("Multiplication =", num1 * num2)

        elif operation == "d":
            if num2 != 0:
                print("Division =", num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")

        else:
            print("Invalid operation selected.")

    except ValueError:
        print("Please enter valid numeric values.")

elif choice == "2":

    print("""
Which conversion do you want?
a. Rupees to other currencies
b. Kilometre to smaller units
c. Celsius to other temperature units
""")

    unit_choice = input("Enter your choice (a/b/c): ")

    if unit_choice == "a":
        money = float(input("Enter amount in Rupees: "))

        print(f"{money} Rupees = {money / 88.68:.2f} USD")
        print(f"{money} Rupees = {money * 0.0178:.2f} Yen")
        print(f"{money} Rupees = {money * 0.00978:.2f} Euro")
        print(f"{money} Rupees = {money * 0.00861:.2f} Pound")

    elif unit_choice == "b":
        distance = float(input("Enter distance in Kilometres: "))

        print(f"{distance} km = {distance * 1000} metres")
        print(f"{distance} km = {distance * 10000} decimetres")
        print(f"{distance} km = {distance * 100000} centimetres")
        print(f"{distance} km = {distance * 1000000} millimetres")

    elif unit_choice == "c":
        temp = float(input("Enter temperature in Celsius: "))

        print(f"{temp} °C = {temp + 273.15:.2f} Kelvin")
        print(f"{temp} °C = {(temp * 9/5) + 32:.2f} Fahrenheit")
        print(f"{temp} °C = {temp * (4/5):.2f} Reaumur")

    else:
        print("Invalid option selected.")

else:
    print("Please select a valid option.")