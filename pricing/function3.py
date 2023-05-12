from function1 import calculatePrice1
from function2 import calculatePrice2

def calculatePrice3(options):
    if options['drink_type'] != 'hot':
        raise ValueError("Chocolate sauce can only be added to hot drinks.")

    base_price = calculatePrice1(options)

    num_pumps = int(input("How many pumps of chocolate sauce would you like? (max 6): "))
    if num_pumps < 0 or num_pumps > 6:
        raise ValueError("Invalid number of pumps selected. Please choose a value between 0 and 6.")

    # First 2 pumps are free
    extra_pumps = num_pumps - 2
    if extra_pumps > 0:
        # $0.5 for each extra pump
        base_price += 0.5 * extra_pumps

    return base_price

options = {
    'drink_type': 'hot',
    'size': input("Select size (S, M, or L): "),
    'whipped_cream': input("Select whipped cream topping (with or without): "),
    'availability_L_size': (input("Is L size available for this drink type? (y/n): ").lower() == 'y'),
}

try:
    price = calculatePrice3(options)
    print("Price: $", price)
except ValueError as e:
    print("Error:", str(e))
