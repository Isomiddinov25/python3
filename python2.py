def capitalize_word(word):
    if len(word) == 0:
        return word  # If the word is empty, return it as is
    return word[0].upper() + word[1:]

# Examples:
print(capitalize_word("hello"))  # Output: "Hello"
print(capitalize_word("Hello"))  # Output: "Hello" (already capitalized)
print(capitalize_word("a"))      # Output: "A"
