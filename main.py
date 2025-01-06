from customer import User
from database import *

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = User(username,password)
    db_user = Database(username=username, password=password, balance=0)  # Temporary balance

    if db_user.user_exists(username):
        print("Welcome back! Your account already exists.")
        current_balance = db_user.get_balance()
        if current_balance is not None:
            print(f"Your current money is: {db_user.formatted_vnd(current_balance)} VND")
        else:
            print("Error retrieving balance.")
    else:
        print("Welcome! Your account does not exist.")
        try:
            user.current_money = int(input("Please enter your current money: "))
        except ValueError:
            print("Invalid amount entered. Please enter a valid number.")
            return

        db_user.balance = user.current_money
        db_user.store_user_in_database()
        print("Your account has been created successfully!")


if __name__ == "__main__":
    main()