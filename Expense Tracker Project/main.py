# Expense Tracker Project

expenses = []; #Lists of expenses in form of dictionaries

print("WELCOME TO THE EXPENSE TRACKER APP"); 

while True:
    print("===MENU==="); 
    print("1. Add Expense"); 
    print("2. View Total Expenses");
    print("3. View Total Spending");
    print("4. Exit");

    choice = int(input("Enter your choice: ")); 

    if choice == 1:
        date = input("Enter expense Date (DD-MM-YYYY): "); 
        category = input("Enter expense category (Food, Games, Travel, etc): "); 
        description = input("Enter short description: "); 
        amount = float(input("Enter expense amount: ")); 

        expense = {"date" : date,
                   "category" : category,
                   "description" : description,
                   "amount" : amount};
        expenses.append(expense);
        print("✅Expense added successfully!");
