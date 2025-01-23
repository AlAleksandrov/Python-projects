num = int(input())
k = 0

for i in range((2 * num) - 1):
    for j in range(i):
        if i < num:
            print("*", end="")
        else:
            k = j
            j = (2 * num) - i - 2
            for _ in range(j):
                print("*", end="")
            j = k
            break
    print("*")
