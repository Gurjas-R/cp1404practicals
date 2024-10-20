"""Word Occurences
Estimate: 20 minutes
Actual:

This program counts the occurrences of each word in a given string,
sorts them, and prints them in an aligned format.
"""
text = input("Text: ")

# Split the text into words and count occurrences
word_counts = {}
words = text.split()

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Sort the dictionary
sorted_words = sorted(word_counts.keys())

# Find the longest word for formatting in print
max_length = max(len(word) for word in sorted_words)
for word in sorted_words:
    print(f"{word:{max_length}} : {word_counts[word]}")