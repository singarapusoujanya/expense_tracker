from expense import add_expense, view_expenses, total_expense,show_graph

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Show Graph")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        add_expense(amount, category)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        show_graph()
        
    elif choice == "5":
        break

    else:
        print("Invalid choice")