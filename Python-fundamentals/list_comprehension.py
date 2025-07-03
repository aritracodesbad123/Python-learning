words = ["apple", "banana", "orange", "umbrella", "idea", "sky", "eye", "egg", "grape"]
vowels = ["a","e","i","o","u"]
vowel_words = [x for x in words if (x[0] in vowels and x[-1] in vowels) ]
print(vowel_words)

