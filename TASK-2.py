amount = 10000
balance = amount
pin = "0000"
attempts = 4

print("-" * 40)
print("          WELCOME TO ATM          ")
print("-" * 40)

print("""
What do you want to do?
1. Check Balance
2. Withdraw Money
3. Deposit Money
""")

choice = input("Enter your option (1/2/3): ")

if choice == "1":

    while attempts > 0:
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print("Your available balance is:", balance)

            ask = input("Do you want to withdraw money? (y/n): ")
            if ask.lower() == "y":
                withdraw = float(input("Enter amount to withdraw: "))

                if withdraw <= balance:
                    balance -= withdraw
                    print("Successfully withdrawn:", withdraw)
                    print("Remaining balance:", balance)
                else:
                    print("Insufficient balance.")
            break

        else:
            attempts -= 1
            print("Incorrect PIN.")
            if attempts > 0:
                print("Attempts left:", attempts)
            else:
                print("No attempts left. Your card is blocked.")

elif choice == "2":

    while attempts > 0:
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print("Your available balance is:", balance)

            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw <= balance:
                balance -= withdraw
                print("Successfully withdrawn:", withdraw)
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance.")
            break

        else:
            attempts -= 1
            print("Incorrect PIN.")
            if attempts > 0:
                print("Attempts left:", attempts)
            else:
                print("No attempts left. Your card is blocked.")

elif choice == "3":

    while attempts > 0:
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print("Your available balance is:", balance)

            deposit = float(input("Enter amount to deposit: "))
            balance += deposit

            print("Successfully deposited:", deposit)
            print("Current balance:", balance)1
            
            break

        else:
            attempts -= 1
            print("Incorrect PIN.")
            if attempts > 0:
                print("Attempts left:", attempts)
            else:
                print("No attempts left. Your card is blocked.")

else:
    print("Please select a valid option (1/2/3).")