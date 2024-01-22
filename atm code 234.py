balance=int(input("Enter Balance"))

while True:
    print("Welcome to the ATM!")
    print("Please select an option:")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit funds")
    print("4. Exit")

    option = input("Enter option number: ")

    if option == '1':
        print("Your balance is",balance, "dollars.")
    elif option == '2':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance == amount
            print("Withdrawal successful.")
    elif option == '3':
        amount = float(input("Enter amount to deposit: "))
        balance == amount
        print("Deposit successful.")
    elif option == '4':
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid option. Please try again.")
