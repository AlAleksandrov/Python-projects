first_string = input()
second_string = input()
printed_string = first_string

for index1 in range(len(first_string)):
    left_side = second_string[:index1 + 1]
    right_side = first_string[index1 + 1:]
    new_string = left_side + right_side
    if printed_string == new_string:
        continue
    else:
        printed_string = new_string

    print(f"{printed_string}")
