from user import User
import random
class Admin:
    def __init__(self,name,email,address,password):
        self.name = name 
        self.email = email
        self.address = address
        self.password = password
        self.balance = 0
        self.users = {}
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
            account_number = str(random.randint(100, 999))
            while account_number in self.users:
                account_number = str(random.randint(100, 999))
            new_user = User(name, email, address, account_type)
            self.users[account_number] = new_user
            print(f"Account created successfully for {name}. Account Number: {account_number}")
            return account_number

    def delete_account(self, account_num):
        if account_num in self.users:
            del self.users[account_num]
            print(f"Account with account number {account_num} has been deleted.")
        else:
            print("Account not found.")


  

    # def find_user(self, account_number):
    #     return self.users.get(account_number,None)

        

    def view_all_user(self):
        if not  self.users:
            print("Users not found")
        else:
            print("All the users:")
            for account_number, user in self.users.items(): 
                print(f"Name: {user.name}, Email: {user.email},Account Number: {account_number} Balance: {user.balance}")
        


    def check_bank_balance(self):
        total_bal = sum(user.balance for user in self.users.values())
        print(f"The total balance of the bank is : {total_bal}")
        return total_bal 

    def check_total_loans_amount(self):
        total_loan = sum(user.loan_taken for user in self.users.values())
        print(f"The total loan taken  from the bank is : {total_loan}")
        return total_loan
    

    def on_off_loan_feature(self,status):
        self.loan_feature = status
        # print(f"Loan feature is now {'ON' if status else 'OFF'}.")
        if status == 'ON':
            print(f"Loan feature is now ON")
        else :
            print(f"Loan feature is now OFF")
        return self.loan_feature
       



