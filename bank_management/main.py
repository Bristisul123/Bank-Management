from admin import Admin
from user import User
from bank import Bank

admin = Admin("Admin", "admin@bank.com", "1/a Admin Street", "123")
bank = Bank("JCP Bank")
bank.admin = admin 


def user_menu():
        
    email = input("Enter Your Email: ")
    user = None
    for account_num, usr in bank.admin.users.items():
      if usr.email == email:
        user = usr
        break
    if user is None:
        print("User not found! Returning to main menu.")
        return
    
    while True:
        print(f"\nWelcome  {user.name} !!")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Transfer Money")
        print("4. Check Balance")
        print("5. Check Transaction History")
        print("6. Take Loan")
        print("7. Check Bank Status")
        print("8. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif choice == 3:
            recipient_account = input("Enter recipient's account number: ")
            if recipient_account in bank.admin.users:
                recipient = bank.admin.users[recipient_account]
                amount = float(input(f"Enter amount to transfer to {recipient.name}: "))
                user.transfer(amount, recipient)
            else:
                print("Recipient account not found.")
        elif choice == 4:
            user.check_available_balance()
        elif choice == 5:
            user.check_transaction_history()
        elif choice == 6:
            # if bank.admin.loan_feature:
            if bank.admin.loan_feature:
                amount = float(input("Enter loan amount: "))
                user.take_loan(amount)
            else : 
                print("Cann't give you loan. Contact with the admin")

        elif choice == 7 :
             bank.check_bank_status()

        elif choice == 8:
            break
        else:
            print("Invalid choice. Try again.")



def admin_menu(bank):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. View All Users")
        print("4. Check Bank Balance")
        print("5. Check Total Loan amount")
        print("6. On/Off Loan Feature")
        print("7. Check Bank Status")
        print("8. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1: 
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.admin.create_account(name, email, address, account_type)
        elif choice == 2:
            account_num = input("Enter account number to delete: ")
            bank.admin.delete_account(account_num)
        elif choice == 3:
            bank.admin.view_all_user()
        elif choice == 4:
            bank.admin.check_bank_balance()
        elif choice == 5:
            bank.admin.check_total_loans_amount()
        elif choice == 6:
            status = input("Turn loan feature ON or OFF? (ON/OFF): ").strip().upper()
            if status == "ON":
                bank.admin.on_off_loan_feature(True)
            elif status == "OFF":
                bank.admin.on_off_loan_feature(False)
            else:
                print("Invalid input.")
        
        elif choice == 7:
             bank.check_bank_status()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Try again.")



while True:
        print(f"\n Welcome to {bank.bank_name}  ")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            admin_menu(bank)
        elif choice == 2:
              user_menu()
        elif choice == 3:
            print(f"Thank you for using {bank.bank_name}. Hope to see you again.")
            break
        else:
            print("Invalid choice. Try again.")