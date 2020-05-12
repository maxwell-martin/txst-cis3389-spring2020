# Exercise 1
dic1 = { 1:10, 2:20, 3:30, 4:40, 5:50, 6:60 }
dic1_values = list(dic1.values())
print(dic1_values)


# Exercise 2
msg = "Welcome to CIS3389. CIS3389 is a .3- credit course. This course meets at 3:00 pm. This course has more than 45 students."
msg_partitions = msg.partition("3-")
print(msg_partitions)
print(msg_partitions[1][0])
# or, her way
b = msg.split()
print(b[6])
print(b[6].rstrip("-"))
# Display words without punctuation
print(b[6].strip(".-"))
for word in b:
    print(word.strip(".,?!-:"), end = " ")
print()


# Exercise 3 - a.
import os
path = r"D:\college_pcfd\spring_2020\CIS3389.251_Python\in_class\Q3"
in_files = os.listdir(path)
print("Filename\tCount")
for filename in in_files:
    filepath = os.path.join(path, filename)
    file = open(filepath)
    count = 0
    for line in file:
        count += line.count("CIS3389")
    print(filename, "\t", count)
    file.close()
print()


# Exercise 3 - b.
print("Filename\t Line")
for filename in in_files:
    filepath = os.path.join(path, filename)
    file = open(filepath)
    for line in file:
        if "python" in line.lower():
            print(filename, "\t", line.replace('\n', ""))
    file.close()
print()


# Exercise 3 - c.
path = r"D:\college_pcfd\spring_2020\CIS3389.251_Python\in_class\Q3_Copy"
print("Filename\t Line")
for filename in in_files:
    filepath = os.path.join(path, filename)
    file = open(filepath)
    file_text = file.read()
    for sentence in file_text.split("."):
        if "python" in sentence.lower():
            print(filename, "\t", sentence.strip())
    file.close()
print()


# Exercise 4
nums =  [55, 652, 38]
try:
    index = int(input("Enter an index: "))
    print(nums[index])
except ValueError as err:
    print("Please enter an integer - Message:", err)
except IndexError as err:
    print("Please enter a valid index - Message:", err)
except Exception as err:
    print("Invalid input - Message:", err)
print()


# Exercise 5
nums = []
num = int(input("Enter an integer: "))
while num > 0:
    nums.append(num)
    num = int(input("Enter an integer: "))
print(nums)
print("Total:", sum(nums))
print()


# Exercise 6
string = 'I like python and I use Python in CIS3389 course'
words = string.lower().split()
lengths = []
for word in words:
    lengths.append(len(word))
max_len_idx = lengths.index(max(lengths))
min_len_idx = lengths.index(min(lengths))
print("Smallest:", words[min_len_idx], "- Length:", lengths[min_len_idx])
print("Largest:", words[max_len_idx], "- Length:", lengths[max_len_idx])
