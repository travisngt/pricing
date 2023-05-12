def calculatePrice4(options):
    if options['item_type'] not in ['sandwich', 'bagel']:
        raise ValueError("Invalid item type selected.")

    base_price = 3

    if options['item_type'] == 'sandwich':
        if options['sandwich_type'] not in ['egg', 'turkey']:
            raise ValueError("Invalid sandwich type selected.")
        base_price += 1

    elif options['item_type'] == 'bagel':
        if options['topping'] not in ['butter', 'cream cheese']:
            raise ValueError("Invalid bagel topping selected.")
        base_price += 0.5

    return base_price
options = {
    'item_type': input("Select item type (sandwich or bagel): "),
}

if options['item_type'] == 'sandwich':
    options['sandwich_type'] = input("Select sandwich type (egg or turkey): ")
elif options['item_type'] == 'bagel':
    options['topping'] = input("Select bagel topping (butter or cream cheese): ")

try:
    price = calculatePrice4(options)
    print("Price: $", price)
except ValueError as e:
    print("Error:", str(e))
