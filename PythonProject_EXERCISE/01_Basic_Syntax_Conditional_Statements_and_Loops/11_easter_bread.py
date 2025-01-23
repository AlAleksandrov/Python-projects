budget = float(input())
one_kg_flour_price = float(input())
one_pack_of_eggs_price = one_kg_flour_price * ((100 - 25) / 100)
one_liter_milk_price = one_kg_flour_price * ((100 + 25) / 100)
recipe_price = one_pack_of_eggs_price + one_kg_flour_price + one_liter_milk_price / 4
current_bred_count = 0
received_colored_eggs_count = 0

while budget >= recipe_price:
    current_bred_count += 1
    received_colored_eggs_count += 3
    if current_bred_count % 3 == 0:
        received_colored_eggs_count -= current_bred_count - 2
    budget -= recipe_price

print(f"You made {current_bred_count} loaves of Easter bread! \
Now you have {received_colored_eggs_count} eggs and {budget:.2f}BGN left.")
