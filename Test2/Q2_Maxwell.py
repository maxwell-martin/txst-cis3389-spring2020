# Exam 2 - Question 2 - Maxwell Martin


# The string to perform operations on.
test_string = "CIS3389 exam2 is on Monday, not on Wednesday"

# A list of all valid vowels.
vowels = ['a','e','i','o','u']

# Variables to hold a list of vowels from string and a dictionary of vowel
# frequencies.
vowels_in_string = []
vowels_frequencies = {}

# Loop through all characters in the test string.
for char in test_string:
    # Convert character to lowercase for consistency.
    lower_char = char.lower()

    # First, check if the character is a vowel.
    if lower_char in vowels:
        # Check if vowel is not in the list of vowels from string.
        if lower_char not in vowels_in_string:
            # Add vowel to list.
            vowels_in_string.append(lower_char)

        # Check if vowel is a key in frequencies dictionary.
        if lower_char in vowels_frequencies.keys():
            # Increment frequency of vowel.
            vowels_frequencies[lower_char] += 1
        else:
            # Add vowel to dictionary with a frequency of 1 to start.
            vowels_frequencies[lower_char] = 1

# Print results.
print("String:", test_string, "\n")
print("The list of vowels from the given string:", vowels_in_string, "\n")
print("Vowel Frequencies:")
for key, value in vowels_frequencies.items():
    print(key, "-", value)
