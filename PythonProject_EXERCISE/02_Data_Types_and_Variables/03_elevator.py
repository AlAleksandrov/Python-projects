from math import ceil

persons = int(input())
capacity = int(input())

result = ceil(persons / capacity)

print(f"{result}")
