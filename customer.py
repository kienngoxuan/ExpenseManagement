from datetime import datetime

class User:
    def __init__(self, username, is_new_user):
        self.username = username
        self.is_new_user = is_new_user
        self.current_money = 0
        self.spend_categories = []
        self.spend_money_day = []
        self.receive_categories = []
        self.receive_money_day = []
        
        

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
        while True:
            user_message = input("Receive or Spent? (R/S) \n").strip().lower()
            try:
                if user_message == 'r':
                    self.receive_money()
                    self.time_receive_money()
                    self.add_receive_category()
                elif user_message == 's':
                    self.spend_money()
                    self.time_spent_money()
                    self.add_spent_category()
                break
            except ValueError:
                print("Invalid input. Please try again.\n")

    def receive_money(self):
        while True:
            try:
                add_money = int(input("How much money do you receive? \n"))
                self.current_money += add_money
                print(f"Now, your current money is: {self.current_money}")
                break
            #print("You received more money at: ", datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def time_receive_money(self):
        while True:
            try:
                time_receive_choice = input("When do you receive this money? Today or another day ? (T/A) \n").strip().lower()
                if time_receive_choice == "t":
                    receive_today = datetime.now().strftime('%Y/%m/%d')
                    self.receive_money_day.append(receive_today)
                    print("You received more money at: ", receive_today)
                    print("Your date list of transtractions: ",self.receive_money_day)
                elif time_receive_choice == "a":
                    string_receive_anotherday = input("Enter the day you receive the money (DD/MM/YYYY): \n")
                    receive_anotherday = datetime.strptime(string_receive_anotherday, '%d/%m/%Y')
                    self.receive_money_day.append(receive_anotherday.strftime('%Y/%m/%d'))
                    print("You received more money at: ", receive_anotherday)
                    print("Your date list of transtractions: ",self.receive_money_day)
                break
            except ValueError:
                print("Invalid input. Please try again.\n")
    

    def spend_money(self):
        while True:
            try:
                spent_money = int(input("How much money do you spend? \n"))
                if spent_money > self.current_money:
                    print("You don't have enough money! Please enter correctly\n")
                else:
                    self.current_money -= spent_money
                    print(f"Now, your current money is: {self.current_money}")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def time_spent_money(self):
        while True:
            try:
                time_spent_choice = input("When do you spend this money? Today or another day ? (T/A) \n").strip().lower()
                if time_spent_choice == "t":
                    spent_today = datetime.now().strftime('%Y/%m/%d')
                    self.spend_money_day.append(spent_today)
                    print("You spent money at: ", spent_today)
                    print("Your date list of transtractions: ",self.spend_money_day)
                elif time_spent_choice == "a":
                    string_spent_anotherday = input("Enter the day you spend the money (DD/MM/YYYY): \n")
                    spent_anotherday = datetime.strptime(string_spent_anotherday, '%d/%m/%Y')
                    self.spend_money_day.append(spent_anotherday.strftime('%Y/%m/%d'))
                    print(f"You spent money at:{spent_anotherday}")
                    print("Your date list of transtractions: ",self.spend_money_day)
                break
            except ValueError:
                print("Invalid input. Please try again.\n")


    def add_receive_category(self):
        receive_category = input("What category is this transaction? (Salary, Allowance, Gift, etc.): \n").strip().lower()
        if receive_category.capitalize() not in self.receive_categories:
            self.receive_categories.append(receive_category.capitalize())
        print("Your current categories: ", self.receive_categories)

    def add_spent_category(self):
        spent_category = input("What category is this transaction? (Food, Entertainment, Transportation, etc.): \n").strip().lower()
        if spent_category.capitalize() not in self.spend_categories:
            self.spend_categories.append(spent_category.capitalize())
        print("Your current categories: ", self.spend_categories)
