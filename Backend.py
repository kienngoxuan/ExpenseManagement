from datetime import datetime
categories = []
username = input("What's your username: \n")
password = input("What's your password: \n")
print("Welcome back " + username + "!\n")


current_money = 0
while current_money <= 0:
    current_money = int(input("Enter your current money: \n"))
    if current_money <0:
        print("You can't have negative money! Please enter correctly\n")
user_message = str.lower(input("Receive or Spent? (R/S) \n"))

if user_message == 'r':
    add_money = int(input("How much money do you receive? \n"))
    current_money += add_money
    print("Now, your current money is: ",current_money)
    print("You receive more money at: ", datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

elif user_message == 's':
    while True:
        spent_money = int(input("How much money do you spent? \n"))
        if spent_money > current_money:
            print("You don't have enough money! Please enter correctly\n")
        else:
            break
    current_money -= spent_money
    print("Now, your current money is: ",current_money)
    print("You spend money at:  ", datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

else:
    print("Invalid input. Please try again.\n")
    print("Your current money still remain the same!\n")
    
if user_message == 'r' or user_message == 's':
    category = str.lower(input("What category is this transaction? (Food, Entertainment, Transportation, etc.): \n"))
    if category not in categories:
        categories.append(str.capitalize(category))
    print("Your current categories: ", categories)
