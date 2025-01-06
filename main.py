from customer import User
from database import *

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = User(username, password)
    db_user = Database(username=user.username, password=user.password, balance=user.current_money)
    
    if not db_user.user_exists(user.username):
        user.set_current_money()
        db_user.store_user_in_database()
        print("Welcome! Your account has been created.")
    else:
        print("Welcome back! Your account already exists.")
        current_balance = db_user.get_balance()
        print(" your current money is : ",current_balance)

if __name__ == "__main__":
    main()