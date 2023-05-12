from function1 import calculatePrice1
from function4 import calculatePrice4


def calculatePrice5(items):
    total_price = 0
    price_breakdown = []

    for item in items:
        if item['item_type'] == 'drink':
            price = calculatePrice1(item)
            price_breakdown.append({'name': item['name'], 'price': price})
        elif item['item_type'] == 'food':
            price = calculatePrice4(item)
            price_breakdown.append({'name': item['name'], 'price': price})
        else:
            raise ValueError("Invalid item type selected.")

        total_price += price

    tax = total_price * 0.0725
    total_price += tax

    return {'total_price': total_price, 'price_breakdown': price_breakdown}

items = [
    {'item_type': 'drink', 'name': 'Iced Coffee', 'drink_type': 'cold', 'size': 'M', 'whipped_cream': False, 'availability_L': True},
    {'item_type': 'food', 'name': 'Bagel with Butter', 'topping': 'butter'},
    {'item_type': 'drink', 'name': 'Latte', 'drink_type': 'hot', 'size': 'S', 'whipped_cream': True},
]

price_info = calculatePrice5(items)

print("Total Price: $", price_info['total_price'])
print("Price Breakdown:")
for item in price_info['price_breakdown']:
    print(item['name'], " - $", item['price'])
