number = int(input())
capacity = 0

for litres in range(number):
    liters_of_water = int(input())
    if capacity + liters_of_water > 255:
        print("Insufficient capacity!")
        continue
    else:
        capacity += liters_of_water

print(f"{capacity}")
