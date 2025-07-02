students = {
    "Alice": 91,
    "Bob": 65,
    "Charlie": 78,
    "David": 59,
    "Eve": 88,
    "Frank": 73
}

response = {key:value for key,value in students.items() if value>=75}

print(response)