number = int(input())

for num in range(1, number + 1):
    is_special = ""
    while num != number + 1:
        sum_digits = 0
        for x in range(0, len(str(num))):
            string = str(num)
            digit = int(string[x])
            sum_digits += digit
        if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
            is_special = "True"
        else:
            is_special = "False"
        break
    print(f"{num} -> {is_special}")