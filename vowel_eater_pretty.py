word_without_vowels = ""

# Prompt the user to enter a word
prompt = "Enter a word: "
# and assign it to the user_word variable.
user_word = input(prompt)
user_word = user_word.upper()
vowels = ['A', 'E', 'I', 'O', 'U']

for letter in user_word:
    # Complete the body of the loop.
    if letter in vowels:
        continue
    x = letter
    word_without_vowels += x

# Print the word assigned to word_without_vowels.
print(word_without_vowels)
