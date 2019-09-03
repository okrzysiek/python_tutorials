inventory = ["miecz", "zbroja", "tarcza", "napój"]

for item in inventory:
    print(item)


chest = ["złoto", "klejnoty"]

inventory += chest

print(inventory)

inventory[0] = "kusza"
print(inventory)

inventory[4:6] = ["śmieci"]

print(inventory)

del inventory[1]

print(inventory)

del inventory[:]
print(inventory)

