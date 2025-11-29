def greet(name):
    print("Hello", name)
    print("Welcome to the Student Report System")
    print("-" * 40)
    
greet("Nitish")

def subjects(*args):
    print("Subjects Registered:")
    for sub in args:
        print("->", sub)
    print("-" * 40)

subjects(
    "Discrete Mathematics",
    "Linux",
    "Physics",
    "Chemistry",
    "Business Model",
    "TDP",
    "Photography"
)

def calculate(m1, m2, m3, m4, m5, m6, m7):
    total = m1 + m2 + m3 + m4 + m5 + m6 + m7
    percentage = total / 7
    return total, percentage

import random
roll_number = random.randint(1000, 9999)

print("Roll Number:", roll_number)
print("Enter marks out of 100\n")

try:
    maths = int(input("Maths Marks: "))
    linux = int(input("Linux Marks: "))
    physics = int(input("Physics Marks: "))
    chemistry = int(input("Chemistry Marks: "))
    business = int(input("Business Model Marks: "))
    tdp = int(input("TDP Marks: "))
    photography = int(input("Photography Marks: "))

    total, percent = calculate(
        maths, linux, physics, chemistry, business, tdp, photography
    )

    print("\nReport Card")
    print("-" * 40)
    print("Total Marks:", total)
    print("Percentage:", round(percent, 2))

    if percent >= 90:
        grade = "A+"
    elif percent >= 75:
        grade = "A"
    elif percent >= 60:
        grade = "B"
    elif percent >= 40:
        grade = "C"
    else:
        grade = "F"

    print("Grade:", grade)

except ValueError:
    print("Invalid input. Marks should be numbers only.")

except ZeroDivisionError:
    print("Division error occurred.")

import datetime
print("-" * 40)
print("Report Generated on:", datetime.datetime.today())
print("Hope you are doing well.")