from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker1 = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


def bootup():
    """ Startup the machine and take orders"""
    start = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if start == 'off':
        print("Coffee machine shutting down")
    elif start == 'report':
        coffee_maker1.report()
        money.report()
        bootup()
    else:
        drink = menu.find_drink(start)
        is_enough_ingredients = coffee_maker1.is_resource_sufficient(drink)
        is_payment_successful = money.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker1.make_coffee(drink)
            bootup()


bootup()
