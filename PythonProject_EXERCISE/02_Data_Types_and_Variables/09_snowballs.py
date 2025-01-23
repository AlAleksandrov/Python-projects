number_of_snowballs = int(input())
highest_weight = 0
highest_time = 0
highest_quality = 0
highest_value = 0

for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > highest_value:
        highest_weight = snowball_weight
        highest_time = snowball_time
        highest_quality = snowball_quality
        highest_value = int(snowball_value)

print(f"{highest_weight} : {highest_time} = {highest_value} ({highest_quality})")
