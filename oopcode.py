#Object is always for class

# class is a blueprint  that how object will behave
class Atm:

    # Function vs methods
    # Method is a special function written inside the class alos use to its class object 
    # Function is available for all the classes 
    def __init__(self):  # __init__  = Constructor it is a special method 
        self.pin = ""        # which run  inside the code automatically 
        self.balance = 0  # execute when we make the object  of this class
        self.menu()
    def menu(self):
        user_input = input("""
        Hello How would you like to proceed ?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
""")
        if user_input == '1':
          self.create_pin()
        elif user_input == '2':
          self.deposit()
        elif user_input == '3':
          self.withdraw()
        elif user_input == "4":
          self.check_balance()
        else:
          print(exit)
    
    def create_pin(self):
        self.pin = input("Enter your Pin")
        print("Pin Set successfully ")
        
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit successfully")
        else:
            print("Invalid pin")
    
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount  = int(input("Enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("operational successful")
            else:
                print("Insufficient  fund")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")

sbi = Atm()
sbi.deposit()
sbi.deposit()
sbi.check_balance()
sbi.withdraw()
sbi.check_balance()








        









     


    