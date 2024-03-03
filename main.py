#project: Building coffee machine using OOP

# import the required modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

profit = 0
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

# create a while loop to keep the program running until the user exits
to_make = input("Enter 'on' to turn on the machine and 'off' to turn off the machine: ")
while to_make == 'on':
  choice = input(f"choose one:{my_menu.get_items()}/reoprt: ")

  # check if the ser input is in the menu, else keep asking
  while choice.lower() not in ('espresso', 'latte', 'cappuccino', 'report'):
    choice = input(f"choose one:{my_menu.get_items()}/report: ")
    
  if choice.lower() == 'report':
    my_coffee_maker.report()
    my_money_machine.report()
  else:
    drink = my_menu.find_drink(choice)
    print(f"the price for {choice} is ${drink.cost}")
    
     # check if there are enough ingredients and the money paid is emough and if it is, make the coffee.
    if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
      my_coffee_maker.make_coffee(drink)
      
  #     ask the user if they want to continue or turn off the mahcine    
  prompt2 = input("Enter 'on' to continue and 'off' to turn off the machine: ")
  if prompt2 == 'off':
              break
else:
  to_make = 'off'

