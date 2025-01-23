year = int(input())

while True:
    year += 1
    if len(set(str(year))) == len(str(year)):
        print(f"{year}")
        break
