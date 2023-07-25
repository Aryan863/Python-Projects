MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
    "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 100,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 150,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def user_input():
    '''Used to input coffee type from user. User can also generate a report of available resources'''
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino" or choice == "report":
        return choice
    else:
        return "error"
    
def check_availability(choice):
    '''used to check the availability of resources to build a coffee according to user choice'''
    flag = True
    if choice == "report":
        print(resources)
        print(f"money= {money}")
        return False
    
    req_resources = MENU[choice]["ingredients"]
    for key in req_resources:
        if resources[key] < req_resources[key]:
            print(f"Sorry there is not enough {key}")
            flag = False
    
    return flag

def insert_coins(choice):
    print("Please insert coins: ")
    input_money = int(input("How many rupees?: "))
    if input_money < MENU[choice]["cost"]:
        print("Sorry not enough!! . Money refunded ") 
        return 0
    
    change = input_money - MENU[choice]["cost"]
    decrease_resources(choice)
    print(f"Here is your Rs.{change} change")
    print(f"Here is your {choice}. Enjoy!!!")
    return input_money

def decrease_resources(choice):
    req_resources = MENU[choice]["ingredients"]
    for key in req_resources:
        resources[key]-=req_resources[key]


end = False
while not end:
    choice = user_input()
    available = check_availability(choice)
    if available:
        money+=insert_coins(choice)
    
    cont = input("Do you want to order anyrhing else?: 'y' or 'n' ")
    if cont == "n":
        end = True

