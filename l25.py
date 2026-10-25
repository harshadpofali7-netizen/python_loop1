#program to count consonants in string
text = "Hello World"
vowels = "aeiou"
consonant_count = 0
for char in text:
    if char.isalpha() and char.lower() not in vowels:
        consonant_count += 1
print(f"The number of consonants in '{text}' is: {consonant_count}")
