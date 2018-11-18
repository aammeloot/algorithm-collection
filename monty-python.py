# Counting the word occurrences in a Monty Python sketch

# Function all characters of a word. If non alphanumerical discard it.
# Return stripped word.
def strip_non_alnum(from_word):
    to_word = "" 
    for single_character in from_word:
        if  single_character.isalnum():
            to_word += single_character
    return to_word

# Empty map of the word frequencies
word_frequencies = {}

# Opening the text file in read mode
f = open("monty_python.txt")
# Save all the lines in a single list
all_lines = f.readlines()
f.close()

# Loop: all the individual lines
for single_line in all_lines:
    # Split all the words from a line
    line_words = single_line.split()
    # Nested loop: all the word in a line
    for single_word in line_words:
        # Strip off the single word of sepcial characters
        single_word = strip_non_alnum(single_word)
        # If the word is already in the map add to counter
        if single_word in word_frequencies.keys():
            word_frequencies[single_word] += 1
        else: # Otherwise create map entry
            word_frequencies[single_word] = 1

# Display each word sorted alphabetically with its amount
words = sorted(word_frequencies.keys())
for single_word in words:
    print(single_word,"appears",word_frequencies[single_word],"time(s).")
