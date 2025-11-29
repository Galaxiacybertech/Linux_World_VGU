meal_price = {
    "breakfast": 40,
    "lunch": 70,
    "snacks": 30,
    "dinner": 80
}

meal_tokens = {
    "breakfast": 50,
    "lunch": 60,
    "snacks": 40,
    "dinner": 55
}

meal_time = {
    "breakfast": "morning",
    "lunch": "afternoon",
    "snacks": "evening",
    "dinner": "night"
}

token_cart = []
MAX_TOKENS = 6

print("\nHostel Mess Token Management System\n")

student_type = input("Enter student type (regular/guest): ").lower()

if student_type == "guest":
    extra_charge = 10
    print("Note: Guest students are charged Rs 10 extra per token.\n")
else:
    extra_charge = 0

current_time = input("Enter current time slot (morning/afternoon/evening/night): ").lower()

print("\nAvailable meals:\n")
for meal in meal_price:
    print(
        meal,
        "- Rs",
        meal_price[meal],
        "| Tokens left:",
        meal_tokens[meal],
        "| Time:",
        meal_time[meal]
    )

print("\nType 'done' when finished.\n")

total_tokens_taken = 0

while True:
    meal = input("Enter meal name: ").lower()

    if meal == "done":
        break

    if meal not in meal_price:
        print("Meal not available.\n")
        continue

    if meal_time[meal] != current_time:
        print("This meal is not served at the given time.\n")
        continue

    qty = int(input("Enter number of tokens: "))

    if total_tokens_taken + qty > MAX_TOKENS:
        print("Daily token limit exceeded. Maximum allowed:", MAX_TOKENS)
        continue

    if qty <= meal_tokens[meal]:
        token_cart.append((meal, qty))
        meal_tokens[meal] -= qty
        total_tokens_taken += qty
        print("Tokens added successfully.\n")
    else:
        print("Only", meal_tokens[meal], "tokens available.\n")

total_amount = 0

print("\nMess Receipt\n")
for meal, qty in token_cart:
    cost = (meal_price[meal] + extra_charge) * qty
    total_amount += cost
    print(meal, "x", qty, "= Rs", cost)

if student_type == "regular" and total_amount > 300:
    discount = 50
elif student_type == "regular" and total_amount > 200:
    discount = 30
else:
    discount = 0

final_amount = total_amount - discount

print("\nTotal Amount:", total_amount)
print("Discount:", discount)
print("Final Payable Amount:", final_amount)

payment = input("\nSelect payment method (cash/online): ").lower()
if payment in ["cash", "online"]:
    print("Payment received via", payment)
else:after
    print("Invalid payment mode selected.")

unique_meals = set()
for m, q in token_cart:
    unique_meals.add(m)

print("\nTotal different meals taken:", len(unique_meals))
print("Meals:", unique_meals)

print("\nPlease collect your tokens from the counter.")