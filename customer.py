from datetime import datetime

class User:
    def __init__(self, username, is_new_user):
        self.username = username
        self.is_new_user = is_new_user
        self.current_money = 0
        self.categories = []

    def welcome_user(self):
        if self.is_new_user:
            print(f"Welcome, {self.username}!")
        else:
            print(f"Welcome back, {self.username}!")

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
        user_message = input("Receive or Spent? (R/S) \n").strip().lower()
        if user_message == 'r':
            self.receive_money()
        elif user_message == 's':
            self.spend_money()
        else:
            print("Invalid input. Please try again.\n")

    def receive_money(self):
        try:
            add_money = int(input("How much money do you receive? \n"))
            self.current_money += add_money
            print(f"Now, your current money is: {self.current_money}")
            print("You received more money at: ", datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def spend_money(self):
        while True:
            try:
                spent_money = int(input("How much money do you spend? \n"))
                if spent_money > self.current_money:
                    print("You don't have enough money! Please enter correctly\n")
                else:
                    self.current_money -= spent_money
                    print(f"Now, your current money is: {self.current_money}")
                    print("You spent money at:  ", datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def add_category(self):
        category = input("What category is this transaction? (Food, Entertainment, Transportation, etc.): \n").strip().lower()
        if category.capitalize() not in self.categories:
            self.categories.append(category.capitalize())
        print("Your current categories: ", self.categories)

