from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


mymenu = Menu()

mycoffee_maker = CoffeeMaker()
mymoney_machine = MoneyMachine()

is_on = True

# latte = MenuItem('Latte', 10, 80, 10, 100)
# capachino = MenuItem('Capachino', 70, 10, 20, 80)
# expresso = MenuItem('Expresso', 50, 40, 10, 90)

mycoffee_maker.report()
mymoney_machine.report()

while is_on:
    options = mymenu.get_items()
    choice = input(f'What would you like? ({options}): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        mycoffee_maker.report()
        mymoney_machine.report()
    else:
        drink = mymenu.find_drink(choice)
        if mycoffee_maker.is_resource_sufficient(drink) and mymoney_machine.make_payment(drink.cost):
                mycoffee_maker.make_coffee(drink)