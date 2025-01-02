from customer import User

def main():
    username = input("What's your username: \n").strip()
    is_new_user = input("Are you a new user? (Y/N) \n").strip().lower() == 'y'

    user = User(username, is_new_user)
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
    main()
