food=[("Pizza",400),("Burger",150),("Pasta",160),("Ice Cream",60)]

food_items=sorted(food, key=lambda item: item[1], reverse=True)

print("Food items sorted by price (descending):")
for item in food_items:
    print(f"{item[0]} : Rs.{item[1]}")
