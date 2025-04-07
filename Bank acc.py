class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        """Initialize the Bank Account with user-provided details."""
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account and return the deposited amount."""
        if amount > 0:
            self.balance += amount
            print(f"Ksh {amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw money if sufficient balance is available."""
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Ksh {amount} withdrawn successfully.")

    def check_balance(self):
        """Print the current balance."""
        print(f"Current Balance: Ksh {self.balance:.2f}")

    def customer_details(self):
        """Print customer details."""
        print("\nCustomer Details:")
        print("----------------------------")
        print(f"Customer Name      : {self.customer_name}")
        print(f"Account Number     : {self.account_number}")
        print(f"Date of Opening    : {self.date_of_opening}")
        print(f"Account Balance    : Ksh {self.balance:.2f}")

# Get user input
account_number = input("Enter Account Number: ")
customer_name = input("Enter Customer Name: ")
date_of_opening = input("Enter Date of Account Opening (YYYY-MM-DD): ")
initial_balance = float(input("Enter Initial Balance: "))

# Create a BankAccount object with user input
customer_account = BankAccount(account_number, customer_name, date_of_opening, initial_balance)

# Allow user to perform transactions
while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Customer Details")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        customer_account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        customer_account.withdraw(amount)

    elif choice == "3":
        customer_account.check_balance()

    elif choice == "4":
        customer_account.customer_details()

    elif choice == "5":
        print("Exiting... Thank you for banking with us!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
