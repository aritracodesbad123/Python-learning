nums = [2, 8, 5, 3, 6, 8, 9, 12, 13, 17, 12, 14]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
squares = list(map(lambda x: x ** 2, even_nums))

print("Squares of even numbers:", squares)