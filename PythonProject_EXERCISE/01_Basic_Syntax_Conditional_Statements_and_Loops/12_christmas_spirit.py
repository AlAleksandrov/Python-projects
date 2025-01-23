quantity_of_decorations = int(input())
days_left = int(input())
ornament_set_price = 2
points_ornament_set = 5
tree_skirt_price = 5
points_tree_skirt = 3
tree_garland_price = 3
points_tree_garland = 10
tree_light_price = 15
points_tree_light = 17
total_cost = 0
total_spirit = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        total_spirit += points_ornament_set
    if day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += points_tree_skirt + points_tree_garland
    if day % 5 == 0:
        total_cost += tree_light_price * quantity_of_decorations
        total_spirit += points_tree_light
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_cost += tree_skirt_price + tree_garland_price + tree_light_price
        total_spirit -= 20

if days_left % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
