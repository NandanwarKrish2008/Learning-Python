# Expense Tracker Project

expenses = [] #Lists of expenses in form of dictionaries

print("WELCOME TO THE EXPENSE TRACKER APP") 

while True:
    print("===MENU===") 
    print("1. Add Expense")
    print("2. View Total Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Enter your choice: ")) 

    # Add Expense
    if choice == 1:
        date = input("Enter expense Date (DD-MM-YYYY): ") 
        category = input("Enter expense category (Food, Games, Travel, etc): ") 
        description = input("Enter short description: ") 
        amount = float(input("Enter expense amount: ")) 

        expense = {"Date" : date,
                   "Category" : category,
                   "Description" : description,
                   "Amount" : amount}
        expenses.append(expense)
        print("✅Expense added successfully!")
    # View Total Expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses added yet!") 
        else:
            print("=== Total Expenses ===")
            count = 1
            for expense in expenses:
                print(f"Expense number {count} -> {expense["Date"]}, {expense["Category"]}, {expense["Description"]}, ${expense["Amount"]}")
                count += 1

    elif choice == 3:
        total = 0;
        for expense in expenses:
            total += expense["Amount"] 
        
        print(f"Total Spending: ${total}")

    elif choice == 4:
        print("Thank you for using the Expense Tracker App!")
        break;

    else:
        print("Invalid choice! Please try again.")