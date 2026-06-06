balance = 1000

while True:
    print("\n--- Banking System ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        print("Current Balance =", balance)

    elif choice == "2":
        amount = float(input("Enter Amount: "))
        balance += amount
        print("Amount Deposited")

    elif choice == "3":
        amount = float(input("Enter Amount: "))

        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")