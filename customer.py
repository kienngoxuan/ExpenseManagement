from datetime import datetime
class User:
    spend_categories = ["Food", "Transportation", "Entertainment", "Shopping", "Health", "Education", "Utilities", "Travel", "Housing", "Other"]
    receive_categories = ["Salary", "Investment", "Gift", "Business", "Allowance", "Bonus", "Loan", "Savings", "Pension", "Other"]
    users = []

    def __init__(self, username, is_new_user, is_old_user):
        self.username = username
        self.is_new_user = is_new_user
        self.is_old_user = is_old_user
        self.current_money = 0
        self.spend_money_day = []
        self.receive_money_day = []

    def welcome_user(self):
        if self.is_new_user:
            print(f"Welcome, {self.username}!")
        elif self.is_old_user:
            print(f"Welcome back, {self.username}!")
        else:
            print("Please choose wisely! (Y/N)")

    def set_current_money(self):
        if self.is_new_user:
            while self.current_money <= 0:
                try:
                    self.current_money = int(input("Enter your current money: \n"))
                    if self.current_money < 0:
                        print("You can't have negative money! Please enter correctly\n")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        else:
            print(f"Your current money is: {self.current_money}")

    def handle_transaction(self):
        while True:
            user_message = input("Receive or Spend? (R/S) \n").strip().lower()
            if user_message == 'r':
                self.receive_money()
                break
            elif user_message == 's':
                self.spend_money()
                break
            else:
                print("Invalid input. Please enter 'R' for Receive or 'S' for Spend.\n")

    def receive_money(self):
        while True:
            try:
                add_money = int(input("How much money do you receive? \n"))
                self.current_money += add_money
                print(f"Now, your current money is: {self.current_money}")
                self.time_receive_money()
                self.choose_category("receive")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def time_receive_money(self):
        while True:
            time_receive_choice = input("When do you receive this money? Today or another day? (T/A) ").strip().lower()
            if time_receive_choice == "t":
                receive_today = datetime.now().strftime('%Y/%m/%d')
                self.receive_money_day.append(receive_today)
                break
            elif time_receive_choice == "a":
                try:
                    string_receive_anotherday = input("Enter the day you receive the money (DD/MM/YYYY): ")
                    receive_anotherday = datetime.strptime(string_receive_anotherday, '%d/%m/%Y')
                    if receive_anotherday.month == 2 and receive_anotherday.day == 29:
                        if receive_anotherday.year % 4 != 0 or (receive_anotherday.year % 100 == 0 and receive_anotherday.year % 400 != 0):
                            raise ValueError("February 29 is only valid in leap years.")
                    self.receive_money_day.append(receive_anotherday.strftime('%Y/%m/%d'))
                    break
                except ValueError as e:
                    print(f"Invalid date! {str(e)}")
                    print("Ensure the format is DD/MM/YYYY and that February 29 is in a leap year.")
            else:
                print("Invalid choice. Please enter 'T' for today or 'A' for another day.\n")



    def spend_money(self):
        while True:
            try:
                spent_money = int(input("How much money do you spend? \n"))
                if spent_money > self.current_money:
                    print("You don't have enough money! Please enter correctly\n")
                else:
                    self.current_money -= spent_money
                    print(f"Now, your current money is: {self.current_money}")
                    self.time_spent_money()
                    self.choose_category("spend")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def time_spent_money(self):
        while True:
            time_spent_choice = input("When do you spend this money? Today or another day? (T/A) ").strip().lower()
            if time_spent_choice == "t":
                spent_today = datetime.now().strftime('%Y/%m/%d')
                self.spend_money_day.append(spent_today)
                break
            elif time_spent_choice == "a":
                try:
                    string_spent_anotherday = input("Enter the day you spend the money (DD/MM/YYYY): ")
                    spent_anotherday = datetime.strptime(string_spent_anotherday, '%d/%m/%Y')
                    self.spend_money_day.append(spent_anotherday.strftime('%Y/%m/%d'))
                    break
                except ValueError:
                    print("Invalid date! Please ensure the format is DD/MM/YYYY.")
                    print("Remember, February 29 is only valid in leap years (e.g., 2024, 2028).")
            else:
                print("Invalid choice. Please enter 'T' for today or 'A' for another day.\n")


    def choose_category(self, transaction_type):
        if transaction_type == "receive":
            print("Choose a category for this receipt:")
            for i, category in enumerate(User.receive_categories, 1):
                print(f"{i}. {category}")
            while True:
                try:
                    choice = int(input("Enter the number corresponding to the category: \n"))
                    if 1 <= choice <= len(User.receive_categories):
                        selected_category = User.receive_categories[choice - 1]
                        if choice == 10:
                            print("You have chosen the 'Other' category. Please enter the category name:")
                            category_name = input()
                            print(f"Transaction categorized as: {category_name}")
                        else:
                            print(f"Transaction categorized as: {selected_category}")
                        break
                    else:
                        print("Invalid choice. Please select a valid category.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif transaction_type == "spend":
            print("Choose a category for this spending:")
            for i, category in enumerate(User.spend_categories, 1):
                print(f"{i}. {category}")
            while True:
                try:
                    choice = int(input("Enter the number corresponding to the category: \n"))
                    if 1 <= choice <= len(User.spend_categories):
                        selected_category = User.spend_categories[choice - 1]
                        if choice == 10:
                            print("You have chosen the 'Other' category. Please enter the category name:")
                            category_name = input()
                            print(f"Transaction categorized as: {category_name}")
                        else:
                            print(f"Transaction categorized as: {selected_category}")
                        break
                    else:
                        print("Invalid choice. Please select a valid category.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    @classmethod
    def add_user(cls, user):
        cls.users.append(user)