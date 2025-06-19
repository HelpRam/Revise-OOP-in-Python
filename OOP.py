# Define a class called 'Atm' which will contain all ATM-related operations
class Atm:
    # Constructor: this special method is called automatically when an object is created
    def __init__(self):
        # Initializing default values
        self.pin = ""           # Stores user's pin
        self.balance = 0        # Stores current balance

        # Show menu when object is created
        self.menu()

    # This method shows the main menu and handles user choices
    def menu(self):
        user_input = input("""
        ===== Welcome to Nic Asia ATM =====
        Please select an option:
        1. Create a PIN
        2. Withdraw Money
        3. Deposit Money
        4. Check Balance
        5. Exit
        Your choice: """)
        
        # Based on input, call the related method
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.withdraw()
        elif user_input == "3":
            self.deposit()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Thank you for using the ATM. Goodbye!")
        else:
            print("Invalid choice. Try again.")
            self.menu()  # Re-show menu on invalid input

    # Method to set a 4-digit PIN
    def create_pin(self):
        self.pin = input("Please enter a 4-digit PIN: ")
        if len(self.pin) == 4 and self.pin.isdigit():
            print(" PIN created successfully!")
        else:
            print(" Invalid PIN. Try again.")
            self.create_pin()

    # Method to withdraw money from the ATM
    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f" Withdrawn {amount}. Remaining balance: {self.balance}")
            else:
                print(" Insufficient Balance.")
        else:
            print(" Incorrect PIN.")

    # Method to deposit money into the ATM
    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print(f" Deposited {amount}. Total balance: {self.balance}")
        else:
            print(" Incorrect PIN.")

    # Method to check account balance
    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print(f" Your current balance is: {self.balance}")
        else:
            print(" Incorrect PIN.")




# Create an object of the Atm class
Nic_Asia = Atm()

# After menu runs once in constructor, you can still access features manually like this:
# Nic_Asia.deposit()
# Nic_Asia.withdraw()
