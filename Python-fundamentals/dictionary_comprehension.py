students = {
    "Alice": 91,
    "Bob": 65,
    "Charlie": 78,
    "David": 59,
    "Eve": 88,
    "Frank": 73
}


#without dictionary comprehension
passed_students ={}
for key,value in students.items():
    if value>=75:
        passed_students[key] = value

#with dictionary comprehension
response = {key:value for key,value in students.items() if value>=75}

print(passed_students) #Output without comprehension
print(response) #Output with comprehension

