number = int(input())

for index1 in range(97, 97 + number):
    for index2 in range(97, 97 + number):
        for index3 in range(97, 97 + number):
            print(f"{chr(index1)}{chr(index2)}{chr(index3)}")
