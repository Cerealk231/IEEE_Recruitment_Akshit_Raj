# Program to find palindromes in a paragraph

def is_palindrome(word):
    return word == word[::-1]

# Input paragraph
paragraph = input("Enter a paragraph (max 100 words): ")

# Split into words and remove punctuation
words = [w.strip(".,!?;:").lower() for w in paragraph.split()]

# Find palindromes
palindromes = [w for w in words if is_palindrome(w)]

if palindromes:
    print("Palindromes found:", " ".join(palindromes))
else:
    print(0)
