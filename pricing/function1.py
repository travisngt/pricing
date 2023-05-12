def calculatePrice1(options):
    base_price = 2.0
    if options['drink_type'] == 'blended':
        base_price += 1.0
    if options['size'] == 'M':
        base_price += 0.5
    elif options['size'] == 'L':
        base_price += 1.0
        if not options['availability_L_size']:
            raise ValueError("L size not available for this drink type")
    if options['whipped_cream'] == 'with':
        base_price += 0.5
    return base_price
options = {
    'drink_type': input("Select drink type (hot, cold, or blended): "),
    'size': input("Select size (S, M, or L): "),
    'whipped_cream': input("Select whipped cream topping (with or without): "),
    'availability_L_size': (input("Is L size available for this drink type? (y/n): ").lower() == 'y')
}

try:
    price = calculatePrice1(options)
    print("Price: $", price)
except ValueError as e:
    print("Error:", str(e))

