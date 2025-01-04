from customer import User
from database import *

def main():
    while True:
        is_new_user_input = input("Are you a new user? (Y/N) \n").strip().lower()
        if is_new_user_input in ['y', 'n']:
            is_new_user = is_new_user_input == 'y'
            break
        else:
            print("Invalid choice. Please enter 'Y' for Yes or 'N' for No.")

    is_old_user = not is_new_user

    user = User(username, is_new_user, is_old_user)
    User.add_user(user)
    user.welcome_user()
    user.set_current_money()

    while True:
        user.handle_transaction()
        continue_choice = input("Do you want to perform another transaction? (Y to continue or press any other key to exit) \n").strip().lower()
        if continue_choice != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
 username = input("What's your username: \n").strip() 
 password = input("What's your password: \n").strip()
 balance = float(input("enter balance: "))
 store_user_in_database(username,password,balance)