#program to count total words in a string
text = input("Enter a string:")
words = text.split()
word_count = len(words)
print(f"Total word count: {word_count}")
