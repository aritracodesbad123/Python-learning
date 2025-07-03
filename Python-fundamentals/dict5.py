#Merging two dictionaries

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

result = dict(dict1)

for key, value in dict2.items():
    result[key] = result.get(key, 0) + value

print(result)