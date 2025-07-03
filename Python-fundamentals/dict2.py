items = {
    "apple": 30,
    "banana": 10,
    "grapes": 40,
    "mango": 50
}

reversed_items ={}

for fruits,price in items.items():
    reversed_items[price] = fruits

print(reversed_items)