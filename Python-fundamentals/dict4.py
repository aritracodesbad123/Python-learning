#Word counter in a sentence

sentence = input("Enter your sentence")

words = {}

word_counter = 1

words_list  = sentence.split()

for word in words_list:
    if word in words:
        words[word.lower()] +=1
    else:
        words[word.lower()] = word_counter

print(words)


