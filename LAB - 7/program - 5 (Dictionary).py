price_dict = {
    "Apple": 250,
    "Banana": 120,
    "Grapes": 300,
    "Milk": 150,
    "Bread": 200
}

quantity_dict = {
    "Apple": 3,
    "Banana": 5,
    "Milk": 1,
    "Bread": 2
}

total_bill = 0
for item in price_dict:
    total_bill += price_dict[item] * quantity_dict.get(item, 0)

print(f"The total bill is: Rs. {total_bill:.2f}")
