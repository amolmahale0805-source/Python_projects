
class ATM:

    def __init__(self,balance,pin):
        self.balance=balance
        self.pin=pin
    
    def check_pin(self):
        try:
           user_pin=int(input("Enter The Pin:"))
           if user_pin==self.pin:
                
                print("Valid PIN")
                return True
           else:
                print("Invalid Pin")
                return False
        except:
            print("Please Enter PIN In Number Format")
            return False
    def check_balance(self):
        if self.check_pin():
            print("Your Balance is:",self.balance)
    def withdraw(self):
        try:
            if self.check_pin():
                amount=int(input(("Enter the Amount:")))
                if amount<=0:
                    print("Invalid Amount")
                elif amount>self.balance:
                    print("Insufficient Balance")
                else:
                    print("Withdraw Successfully")
                    self.balance -= amount
                    print("Remaining Balance:",self.balance)
        except:
            print("Please Enter Amount In Number Format")
    def deposit(self):
        try:
            if self.check_pin():
                amount=int(input("Enter The Amount:"))
            
                if amount>0:
                    self.balance += amount
                    print("Deposit successfully")
                    print("Remaining Balance:",self.balance)
                else:
                    print("Don't Enter Negative Amount !!!")
        except:
           print("Please Enter Amount In Number Format")
    def change_pin(self):
        try:
            if self.check_pin():
                new_pin=int(input("Enter New PIN:"))
                self.pin = new_pin
                print("PIN Changed Successfully")
        except:
           print("Please Enter PIN In Number Fomat")

    def menu(self):

        while(True):

            print("\n1.Check PIN")
            print("\n2.Check Balance")
            print("\n3.Withdraw")
            print("\n4.Deposit")
            print("\n5.Change PIN")
            print("\n6.Exit")

            try:
                choice=int(input("Enter The Choice:"))
            
                if choice==1:
                    self.check_pin()
                elif choice==2:
                    self.check_balance()
                elif choice==3:
                    self.withdraw()
                elif choice==4:
                    self.deposit()
                elif choice==5:
                    self.change_pin()
                elif choice==6:
                    print("Thank You For Using ATM :)")
                    break
                else:
                    print("Invalid Choice..")
            except:
                print("Please Enter Choice In Number Format")
        

s1=ATM(20000,1234)
s1.menu()
            
