menu = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18
        },
        "cost":1.50
    },
    "latte":{
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150
        },
        "cost":2.50
    },
    "cappacino":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100
        },
        "cost":3.00
    }
}

resources = {
    "water":500,
    "coffee":60,
    "milk":250,
    "money": 2.50
}

profit = 0
def transaction(payment, order_rate):
    if payment >= order_rate:
        global profit
        profit += order_rate
        change = round(payment - order_rate,2)
        print(f"here is your change {change}$")
        return True
    else: 
        print(" sorry coins inserted are not enough")
        return False
        

def make_coffee(coffee_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    return "here is your coffee"
        
    
    
    
def process_coins():
    print("insert coins")
    total = int(input("how many quarters"))*0.25
    total += int(input("how many dimes"))*0.10
    total += int(input("how many nickels"))*0.05
    total += int(input("how many pennies"))*0.01
    return total

def show_report():
    print(resources)
    print("profit")
    return

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f" sorry we dont have enough {item}")
            return False
    return True

is_machine_on = True
while is_machine_on:
    choice = input("what would you like to order (espresso/latte/cappacino)")
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        show_report()
    else: drink = menu[choice]
    if check_resources(drink["ingredients"]):
        payment = process_coins()
        if transaction(payment,drink["cost"]):
            make_coffee(choice,drink["ingredients"])
            
                    
    
        
    

