import random

class User:
    def __init__(self,name,email,address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(100, 999)
        self.balance = 0
        self.trans_history = []
        self.loan_taken = 0


    def deposit(self,amount):
            self.balance += amount
            self.trans_history.append(f"Deposited : {amount}")
            print (f"Your amount has been deposit successfully. Current balance is {self.balance}")

    def withdraw (self, amount):
         if amount > self.balance :
              print ("Withdrawal amount exceeded")
         elif amount <= 0:
              print("Your account is empty") 
         else :
              self.balance -= amount
              self.trans_history.append(f"Withdrawn : {amount}")
              print (f"Your amount has been withdrawn successfully. Current balance is {self.balance}")


    def check_available_balance(self):
         print(f"Your available balance : {self.balance}")
         return self.balance

    def check_transaction_history(self):
          print("Your transaction history:")
          for transaction in self.trans_history:
               print(transaction)

    def take_loan(self,amount):
         if self.loan_taken > 1 :
               print("Error: Loan limit exceeded ")
         else:
              self.balance += amount
              self.loan_taken += amount
              self.trans_history.append(f"Loan taken :{amount}")
              print (f"Your loan has been approaved. Your current balance is: {self.balance}")
              
         return self.balance
              

    def transfer(self,amount,other_user_account ):
         if amount > self.balance:
              print ("Error :Your Balance is low")

         else :
              self.balance -= amount
              other_user_account.balance += amount
              self.trans_history.append(f"Transferred {amount} to {other_user_account.name}")
              other_user_account.trans_history.append(f"Received {amount} from {self.name}")
              print (f"transfered {amount} to {other_user_account.name} successfully.")



