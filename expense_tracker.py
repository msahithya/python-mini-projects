expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Show Total Expense")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense added!")

    elif choice == "2":
        print("Total Expense:", sum(expenses))

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
