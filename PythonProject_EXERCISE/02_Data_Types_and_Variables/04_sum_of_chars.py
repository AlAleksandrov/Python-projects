number_of_lines = int(input())
total_sum = 0

for line in range(number_of_lines):
    letter_per_line = input()
    total_sum += ord(letter_per_line)

print(f"The sum equals: {total_sum}")
