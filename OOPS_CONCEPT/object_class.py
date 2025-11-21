class ATM:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input(''' Hi how can I help you? 
            1. press 1 to create pin
            2. press 2 to change pin
            3. press 3 to check balance
            4. press 4 to withdraw money
            5. press anything to exit \n ''')
        if user_input =='1': # create pin
            self.create_pin()
        elif user_input =='2': # change pin 
            self.change_pin()
        elif user_input =='3': # check balance
            self.check_balance()
        elif user_input =='4': # withdraw balance
            self.withdrw_money()
        else:
            exit()
    def create_pin(self):
        user_pin=input("Enter your pin\n")
        self.pin=user_pin
        bal=int(input("Enter your balance\n"))
        self.balance=bal
        print("pin created succesfully!")
        self.menu()
    def change_pin(self):
        existing_pin=input("Enter your old pin\n ")
        if existing_pin==self.pin: 
            new_pin=input("Enter your new pin\n ")
            self.pin=new_pin
            print("Your new pin change succesfully!")
            self.menu()
            
        else:
            print(" you old pin is incorrect!")
            self.menu()
    def check_balance(self):
        check_pin=input("Enter your pin \n ")
        if check_pin==self.pin:
            print("Your avaiblable balance")
            print(self.balance)
            self.menu()
        else:
            print("invalid pin ")
            self.menu()
    def withdrw_money(self):
        check_pin=input("Enter your pin \n ")
        if check_pin==self.pin:
            print(f"available balance is {self.balance}")
            amount=int(input("How much cash do you need"))
            if amount>self.balance:
                print("you do not have sufficent balance")
            print(f"you have succefully withdrwan Rs {amount}")
            self.balance=self.balance-amount
            print(f" you available balance is Rs {self.balance} now ")
            self.menu()
        else:
            print("you do not have sufficent balance!")
            self.menu()
obj=ATM()
