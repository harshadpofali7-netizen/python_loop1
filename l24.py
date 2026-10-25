text = "Hello World"
vowels = "aeiou"
vowel_count = 0
for char in text:
    if char.lower() in vowels:
        vowel_count += 1
print(f"The number of vowels in '{text}' is: {vowel_count}")
