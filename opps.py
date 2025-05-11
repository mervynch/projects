class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("espresso", 50, 0, 18, 1.5),
            MenuItem("cappuccino", 250, 100, 24, 3.0),
        ]

    def get_items(self):
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None

class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        for resource, amount in self.resources.items():
            print(f"{resource.capitalize()}: {amount}ml" if resource != "coffee" else f"{resource.capitalize()}: {amount}g")

    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy!")

class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: ${self.profit}")

    def make_payment(self, cost):
        print(f"The drink costs ${cost}.")
        payment = float(input("Insert payment: $"))
        if payment >= cost:
            change = round(payment - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry, not enough money. Money refunded.")
            return False
def main():
    is_on = True
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ").lower()
        
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink and coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

if __name__ == "__main__":
    main()