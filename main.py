MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

order = "on"
resources["money"] = 0.0


def get_order():
    global order
    order = input("What would you like? (espresso/latte/cappuccino): ")
    return order


def get_resources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]

    return water, milk, coffee, money


def print_resources():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def get_menu_item(cur_order):
    water_item = MENU[cur_order]["ingredients"]["water"]
    if not cur_order == "espresso":
        milk_item = MENU[cur_order]["ingredients"]["milk"]
    else:
        milk_item = 0
    coffee_item = MENU[cur_order]["ingredients"]["coffee"]
    money_item = MENU[cur_order]["cost"]

    return water_item, milk_item, coffee_item, money_item


def process_coins():
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    quarters_sum = quarters * 0.25
    dimes_sum = dimes * 0.1
    nickles_sum = nickles * 0.05
    pennies_sum = pennies * 0.01
    total_sum = quarters_sum + dimes_sum + nickles_sum + pennies_sum

    return total_sum


def make_coffee():
    resources["water"] -= water_item
    resources["milk"] -= milk_item
    resources["coffee"] -= coffee_item
    resources["money"] += money_item


while not order == "off":
    cur_order = get_order()
    water, milk, coffee, money = get_resources()
    if cur_order == "report":
        print_resources()
    else:
        water_item, milk_item, coffee_item, money_item = get_menu_item(cur_order)
        if water < water_item:
            print("Sorry there is not enough water.")
        elif milk < milk_item:
            print("Sorry there is not enough milk.")
        elif coffee < coffee_item:
            print("Sorry there is not enough coffee.")
        else:
            print(f"The price of {cur_order} is ${money_item}")
            total_sum = process_coins()
            if total_sum < money:
                print("Sorry that's not enough money. Money refunded")
            else:
                change = total_sum - money_item
                if change > 0:
                    print(f"Here is ${change} in change.")
                make_coffee()
                print(f"Here is your {cur_order}. Enjoy!")