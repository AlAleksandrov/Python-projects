number = int(input())
string_number = str(number)
max_number = 0
min_index = 0
total_result = 0
numbers = []
for char in range(len(string_number)):
    num = int(string_number[char])
    if char == 0:
        max_number = num
        min_index = char
        numbers .append(num)
    else:
        if num >= max_number:
            max_number = num
            numbers .insert(min_index, num)
        else:
            min_index1 = 0
            for digit in numbers:
                min_index1 += 1
                if digit <= num:
                    numbers.insert(min_index1 - 1, num)
                    break
            else:
                numbers .append(num)

total_result = ''.join([str(x) for x in numbers])
print(total_result)
