def log_expenses():
    print("Welcome to Daily Expense Tracker!")
    expenses = [] ## we will use an empty list to gather daily expenses 
    Total_Expense = 0 ## we will use variable = 0 to add up all the expenses
    while True:
        expense_name = input("Enter expense name (or type 'end' to finish): ").strip()
        
        if expense_name.lower() == 'end':
            break
        ## then we will use the try function to collect amount info and append it with their names
        try:
            expense_amount = float(input("Enter expense amount: "))
            Total_Expense += expense_amount
            expenses.append((expense_name, expense_amount))
        except ValueError:
            print("Invalid input! Please enter a valid amount.")

    save_expenses(expenses)
            ## this is an if statement that is used to give you info about your total expenses
    if expense_name.lower() == 'end':
        user_input = input('Do you want to check out your total expenses? y / n :').strip().lower()
        if user_input in ['yes', 'y']:
            print(f'Total Expenses = ${Total_Expense}')
        else:
            print("Exiting...")
                  

def save_expenses(expenses):
        ## to save date and time along with the data we will import date and time from python library
    import datetime
    a = datetime.datetime.now()
    time = a.strftime("%Y-%m-%d %H:%M:%S")
    file_name = 'expenses_log.txt'
        ## here we have used an file append operation to add new and newer details to a file
    with open(file_name, 'a') as file:
        for expense in expenses:
            file.write(f"{expense[0]}: ${expense[1]} {time}\n")

    print(f"Expenses saved to {file_name} successfully!")
    
    while True:
            ## here we have used an file aread operation to read from that file
        with open(file_name , 'r') as file:
            a = file.read()
        user_input = input('Do you want to check out your expenses? y / n :').strip().lower()  
        if user_input in ['yes' , 'y']:
            print(a)
            break
        else:
            print("Okay!")
            break

if __name__ == "__main__":
    log_expenses()
