class BankAccount:
    def _ init_(self, accountnumber, name, balance):
        self.accountnumber = accountnumber
        self.name = name
        self.balance = balance
    def deposit(self, ammount):
        if ammount > 0 :
            self.balance += ammount
            print(f"Deposite of Rs.{ammount} succesfull.")
        else:
            print("Invalid Deposite Ammount")
    def withdrawal(self,ammount):
        if 0 < ammount <= self.balance:
            self.balance = ammount
            print(f"Deposite of Rs.{ammount} succesfull.")
        else:
            print("Invalid withdrawl ammount or insufficent ammount")
    def bank_fees(self):
        fee= 0.05*self.balance
        self.balance = fee
        print(f"Bank fees of Rs.{fee} Applied")
    def display(self):
        print(f"Account Number:{self.accountnumber}")
        print(f"Balance : Rs.{self.name}")
        print(f"Account Holder: Rs.{self.balance}")
account1 = BankAccount(accountnumber=123456, name="SumanthDhruva", balance=123)
account1.display()
account1.deposit(500)
account1.withdrawal(200)
account1.bank_fees()
account1.display()