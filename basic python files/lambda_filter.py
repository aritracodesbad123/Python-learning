words =["madam","sky","axa","mom","zombie","momo","zoz"]

filtered_words = list(filter(lambda x:x==x[::-1],words))

print(filtered_words)