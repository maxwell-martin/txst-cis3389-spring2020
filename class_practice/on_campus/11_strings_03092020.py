# Strings

str1 = ' Welcome to CIS3389 class '
str3 = 'Welcome to CIS3389 class'

# Iterating character-wise
#for i in str1:
#    print(i)

# Get character in string via index
print(str1[0]) # Space
print(str1[7]) # e

# Slice and dice a string
print(str1[1:6]) # Welco

# len() method
print(len(str1)) # 26

# Cannot change character in a string
#str1[2] = 'p'
#print(str1)

# Check if substring in string
if 'to' in str1.lower():
    print('found') # Prints found
if 'course' in str1.lower():
    print('found') # Does not print found

# Check if string is alphanumeric
str2 = 'CIS3389'
print(str2.isalnum()) # True
str4 = 'CIS 3389'
print(str3.isalnum()) # False

# Check if string is only alphabet chars
print(str2.isalpha()) # False

# Check if string is only digits
print(str2.isdigit()) # False

# Check if all values are lowercase
print(str2.islower()) # False

# Check if all values are uppercase
print(str2.isupper()) # True

# Check if all values are whitespace characters
print(str2.isspace()) # False

# Remove all leading whitespace characters
print(str1.lstrip())

# Remove all trailing whitespace characters
print(str1.rstrip())

# Remove both leading and trailing whitespace characters
print(str1.strip())

# Remove a specific character
print(str3.lstrip('W'))

# Check if string starts with a specific substring
str5 = 'CIS3389CIS'
print(str5.startswith('CIS')) # True
print(str5.startswith('CIS', 7, len(str5))) # True

# Check if string ends with a specific substring
print(str5.endswith('CIS')) # True

# Find index of substring within string
str6 = 'CIS cis CIS55 cis78 CIS45 CIS67'
print(str6.find('CIS')) # 0

# Replace specific substrings with some other substring
print(str6.replace('CIS', 'kis')) # 'kis cis kis55 cis78'
print(str6.replace('CIS', 'kis', 2)) # 'kis cis kis55 cis78 CIS45 CIS67'

# Split string into list of substrings
print(str3.split())
str3_split = str3.split()
print(str3_split[0] + ',' + str3_split[2])

# Join items in list by string specified
str7 = ','.join(str3_split)
print(str7)

# partition() method
str3_partition = str3.partition('to')
print(str3_partition) # ('Welcome ', 'to', ' CIS3389 class')
print(str3_partition[0]) # 'Welcome '
print(str3_partition[1]) # 'to'
print(str3_partition[2]) # ' CIS3389 class'

# Reverse a string
string1 = "PythonCIS'
rev_str = "".join(reversed(string1))


# Exercise 13
'''string = input("Enter a string: ")
word = input("Enter a word: ")
print(word, "exists", string.count(word), "times.")'''


# Exercise 14
'''string = input("Enter a string: ")
string_split = string.split()
print(','.join(string_split))'''


# Exercise 15
full_name = input("Enter name: ")
name_split = full_name.split()
first_initials = []
for i in name_split:
    first_initials.append(i[0].upper())
for initial in first_initials:
    print(initial, end = '.')
print()


# Exercise 16
string = input("Enter a string: ")
rev_string = ""
for i in range(len(string) - 1, -1, -1):
    rev_string += string[i]
print(rev_string)
# or, her way #1
str_len = len(string)
n1 = []
while str_len >= 1:
    char = string[str_len - 1]
    str_len -= 1
    n1.append(char)
n2 = "".join(n1)
print(n2)


# Exercise 17
string = input("Enter a string: ")
count = 0
string = string.lower()
words = string.split()
for word in words:
    if word[0] == word[-1]:
        count += 1
print("Number of words with first and last letter the same: ", count)
