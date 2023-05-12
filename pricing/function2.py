from function1 import calculatePrice1


def calculatePrice2(options):
    base_price = 2.25 if options['drink_type'] == 'milk tea' else calculatePrice1(options)

    if options['size'] == 'XL':
        base_price += 1.5

    if options['milk_type'] is not None:
        base_price += 0.5 if options['almond_milk'] else 0.0

    return base_price
options = {
    'drink_type': input("Select drink type (hot, cold, blended, or milk tea): "),
    'size': input("Select size (S, M, L, or XL): "),
    'whipped_cream': input("Select whipped cream topping (with or without): "),
    'availability_L_size': (input("Is L size available for this drink type? (y/n): ").lower() == 'y'),
    'size_XL': (input("Do you want XL size? (y/n): ").lower() == 'y'),
    'milk_type': input("Select milk type (whole milk, almond milk, or none): "),
    'almond_milk': (input("Do you want almond milk? (y/n): ").lower() == 'y')
}

try:
    price = calculatePrice2(options)
    print("Price: $", price)
except ValueError as e:
    print("Error:", str(e))
