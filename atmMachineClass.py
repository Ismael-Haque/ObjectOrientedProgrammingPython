class Atm:
    # function vs methods
    # method is a function that is declared inside a class

    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input("""
            Hello, how woluld you like to proceed ?
                1. Enter 1 to create pin
                2. Enter 2 to deposit
                3. Enter 3 to withdraw
                4. Enter 4 to check balance
                5. Enter 5 to quit.
                           
    """)
        
        if user_input == "1":
            self.create_pin()
            self.menu()
        elif user_input == "2":
            self.deposit()
            self.menu()
        elif user_input == "3":
            self.withdraw()
            self.menu()
        elif user_input == "4":
            print("Your balance is ", self.balance)
            self.menu()
        elif user_input == '5':
            print("Bye!")

    def create_pin(self):
        temp_pin = input("Create your pin: ")

        self.pin = temp_pin
        print("Pin created successfully!")
    
    def deposit(self):
        temp_pin = input("Enter your pin: ")
        if temp_pin == self.pin:
            amount = int(input("Input your deposit amount: "))
            if type(amount) == int:
                self.balance = self.balance + amount
                print("Deposit Successful! \n your balance is ", self.balance)
            else:
                print("Balance should only be integer, please try again!")
        else:
            print("wrong pin!")

    def withdraw(self):
        temp_pin = input("Enter your pin: ")

        if temp_pin == self.pin:
            withdrawl_amount = int(input("Enter withdrawl amount: "))
            if withdrawl_amount <= self.balance:
                self.balance = self.balance - withdrawl_amount
                print("withdraw successfull")
            else:
                print("not enough money!")

        else:
            print("Wrong pin! try again!")
    
