# Lab03 Activity - Caburao, Jove Francis Twzi
# String Manipulation Program
input_string = input("Enter a string: ")

# Count vowels, consonants, spaces, and other characters
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
space_count = 0
other_count = 0

for char in input_string:
    if char in vowels:
        vowel_count += 1
    elif char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z':
        consonant_count += 1
    elif char == ' ':
        space_count += 1
    else:
        other_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Spaces:", space_count)
print("Other characters:", other_count)

# This part is printing all words in ascending order
words = []
current_word = ""
for char in input_string:
    if char == ' ':
        if current_word != "":
            words.append(current_word)
            current_word = ""
    else:
        current_word = current_word + char
if current_word != "":
    words.append(current_word)

print("Words in ascending order:")
for word in words:
    print(word)
print()
# Display all words in reverse without changing position
print("Words in reverse:")
for word in words:
    reversed_word = ""
    for i in range(len(word)):
        reversed_word = word[i] + reversed_word
    print(reversed_word, end=" ")
print()

# File Handling and Multiplication Table
row_input = int(input("Enter number of rows (5-20): "))
col_input = int(input("Enter number of columns (5-20): "))

# This converts the negative values to a positive
if row_input < 0:
    rows = -row_input
else:
    rows = row_input
if col_input < 0:
    cols = -col_input
else:
    cols = col_input

# The limit values are 5 to 20
if rows < 5:
    rows = 5
elif rows > 20:
    rows = 20

if cols < 5:
    cols = 5
elif cols > 20:
    cols = 20

# This creates multiplication table and writes to file
f = open("multiplication_table.txt", "w")
for a in range(1, rows + 1):
    for b in range(1, cols + 1):
        result = a * b
        f.write("{:4d}".format(result))
    f.write("\n")
f.close()

print("Multiplication table saved to multiplication_table.txt")