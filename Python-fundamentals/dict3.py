#Square of no.s in a dict

nums = {
    "a": 2,
    "b": 5,
    "c": 3
}

squared_nums = {}
for key,value in nums.items():
    squared_nums[key] = value**2

print(squared_nums)


