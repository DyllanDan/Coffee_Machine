# TODO: 2.Check resources sufficient to make a drink

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 400,
    "milk": 200,
    "coffee": 100,
}

ON = True
MONEY = 0


def cash_input(quarter, dime, nickle, penny):
    money_deposit = 0.25 * quarter + 0.10 * dime + 0.05 * nickle + 0.01 * penny
    return money_deposit


# TODO 8. Check the susses of the transaction
def money_enough(money, price):
    if money >= price:
        return True
    else:
        return False


def available_resources(option):
    a = True
    for machine in MENU[f'{option}']['ingredients']:
        if resources[f'{machine}'] < MENU[f'{option}']['ingredients'][f'{machine}']:
            a = False
            if a == False:
                print(f"There's not enough {machine}")
                return a
        else:
            a = True
        return a


def use_resource(material, order):
    for i in material:
        material[i] = material[i] - MENU[f'{order}']['ingredients'][i]
    return material
#print(MENU['espresso']['ingredients']['milk'])

# TODO: 1. Print report of all the coffee machine resources


ORDER = True


# TODO: 3. ask the user an input (and have to be shown again after)
while ORDER:
    product = input("What would you like? (espresso/latte/cappuccino): ")
    if product == "report":
        print(f" Water: {resources['water']}ml")
        print(f" Milk: {resources['milk']}ml")
        print(f" Coffee: {resources['coffee']}g")
        print(f" Money: ${MONEY}")
    elif product == "off":
        ORDER = False
    else:
        #available_resources(product)
        can_make_coffee = available_resources(product)
        if not can_make_coffee:
            print("Sorry, there isn't enough resources to delivery the product.")
        elif product == "off":
            ORDER = False
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters ($0.25): "))
            dimes = int(input("How many dimes ($0.10): "))
            nickles = int(input("How many nickles ($0.05): "))
            pennies = int(input("How many pennies ($0.01): "))
            total_cash = cash_input(quarters, dimes, nickles, pennies)
            # TODO: check if total_cash is enough
            resources = use_resource(resources, product)
            make_order = money_enough(total_cash, MENU[f'{product}']['cost'])
            change = round(total_cash - MENU[f'{product}']['cost'], 2)
            MONEY += MENU[f'{product}']['cost']

            if make_order:
                print(f"Here's your change ${change}")
                print(f"Here's your {product}, enjoy.")
                #print(resources)
            else:
                print("Cash insufficient. Money refunded.")



# TODO: 4. possible to turn off the machine

# TODO: 6. Check the resources available


# TODO 9. Make the coffee
# TODO 10. Recalculated the resources
