command = input()

while command != "Welcome!":
    name = command
    text = ""
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(name) < 5:
        text = f"{name} goes to Gryffindor."
    elif len(name) == 5:
        text = f"{name} goes to Slytherin."
    elif len(name) == 6:
        text = f"{name} goes to Ravenclaw."
    else:
        text = f"{name} goes to Hufflepuff."
    print(f"{text}")
    command = input()
    if command == "Welcome!":
        print("Welcome to Hogwarts.")
