start_character_index = int(input())
end_character_index = int(input())

for index in range(start_character_index, end_character_index + 1):
    current_character = chr(index)
    if index == end_character_index:
        print(f"{current_character}")
    else:
        print(f"{current_character}", end=' ')
