students = {
    "Ayan": 92,
    "Tina": 76,
    "Mehul": 84,
    "Simran": 67,
    "Raj": 90
}

#without comprehension

Filtered_Studs = {}

for name, score in students.items():
    if score >80:
        Filtered_Studs[name] = score

print(Filtered_Studs)
