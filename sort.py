with open("words.txt") as file:
    lines = file.readlines()
    lines = sorted(lines)
file.close()
with open("words.txt", "w") as file:
    for var in lines:
        file.write(var)