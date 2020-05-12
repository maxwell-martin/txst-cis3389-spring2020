# Opening file in same folder as py file
with open("file1_read.txt", "r") as infile:
    contents = infile.read()       # Returns string of data in file
    contents = infile.readlines()  # Returns List of items
    contents = infile.readline()   # Returns one line as string
    contents1 = infile.readline()
    print(contents)
    print(contents1)
    for line in infile:
        print(line.rstrip("\n"))

infile = open("file1_read.txt", "r") # Sames as with/as
contents = infile.read()
print(contents)
infile.close()


# Opening file from specific folder read()
with open(r"D:\college_pcfd\spring_2020\CIS3389.251_Python\in_class\data\file1_read.txt", "r") as infile:
    contents = infile.read()
    print(contents)


# Writing to a file read() contents
with open(r"D:\college_pcfd\spring_2020\CIS3389.251_Python\in_class\data\file2_read.txt", "w") as outfile:
    contents = infile.read()
    outfile.write(contents)


# Opening file from a specific folder readlines()
with open(r"D:\college_pcfd\spring_2020\CIS3389.251_Python\in_class\data\file1_read.txt", "r") as infile:
    contents = infile.readlines()
    print(contents)


# Writing to a file readlines() contents
with open(r"D:\college_pcfd\spring_2020\CIS3389.251_Python\in_class\data\file3_read.txt", "w") as outfile:
    contents = infile.readlines()
    print(contents, file=outfile)


# Reading multiple files from a folder
import re, os
path = r"D:\college_pcfd\spring_2020\CIS3389.251_Python\in_class\data"
in_files = os.listdir(path)
for file in in_files:
    print(file)
for file in in_files:
    file1 = os.path.join(path, file)
    text = open(file1, "r")
    for line in text:
        print(line.rstrip("\n"))


# Reading from a CSV file
import csv
with open("Enrollment.csv", "r") as infile:
    reader = csv.reader(infile) # Optional arg: delimiter = "\t"
    for row in reader:
        print(row)


# Writing to a CSV file, default adds newline after each writerow with comma delimited
import csv
with open("Course_Enrollment.csv", "w") as infile:
    writer = csv.writer(infile)
    writer.writerow(["ID", "CourseName", "Students enrolled"])
    writer.writerow([1, "CIS3382", 45])
    writer.writerow([2, "CIS3380", 30])


# Writing to a CSV file, no newline after each writerow and \t delimited
import csv
with open("Course_Enrollment.csv", "w", newline = "") as infile:
    writer = csv.writer(infile, delimiter = "\t")
    writer.writerow(["ID", "CourseName", "Students enrolled"])
    writer.writerow([1, "CIS3382", 45])
    writer.writerow([2, "CIS3380", 30])


# Exercise 1
import random

outfile = open("random_number-count.txt", "w")
def main():
    count = 0
    for i in range(30):
        randnum = random.randint(-100, 500)
        if is_negative(randnum):
            count += 1
        #print(randnum, file=outfile)
        outfile.write(str(randnum) + "\n")
    #print("Negative number count:", count, file=outfile)
    outfile.write("Negative number count: " + str(count) + "\n")

def is_negative(num):
    if num < 0:
        return True
    else:
        return False

main()
outfile.close()


### Exercise 2
with open("Numbers.txt", "r") as infile:
    total = 0
    count = 0
    for line in infile:
        total += int(line)
        count += 1
    average = total / count
    print("Count:", count)
    print("Total:", total)
    print("Average:", round(average, 2))


# Exercise 3
import os
path = r"D:\college_pcfd\spring_2020\CIS3389.251_Python\in_class\ex3"
in_files = os.listdir(path)
total = 0
for filename in in_files:
    file = os.path.join(path, filename)
    file = open(file, "r")
    for line in file:
        total += int(line.rstrip("\n"))

print("Sum of all the numbers from all files in ex3 folder:", total)


# Exercise 4
import csv, os
path = r"D:\college_pcfd\spring_2020\CIS3389.251_Python\in_class\ex3"
in_files = os.listdir(path)
with open("file_cumulative_sum.csv", "w", newline="") as outfile:
    total = 0
    writer = csv.writer(outfile)
    writer.writerow(["FileName", "CumulativeSum"])
    print("File Name", "Total for file")
    for filename in in_files:
        file = os.path.join(path, filename)
        file = open(file, "r")
        for line in file:
            total += int(line.rstrip("\n"))
        print(filename, total)
        writer.writerow([filename, total])


# Exercise 5
import csv
with open("file1_read.txt", "r") as infile:
    count = 0
    for line in infile:
        if "course" in line.lower():
            count += 1
##    reader = csv.reader(infile, delimiter = " ")
##    count = 0
##    for row in reader:
##        for word in row:
##            if word.lower() == "course":
##                count += 1
print(count)
