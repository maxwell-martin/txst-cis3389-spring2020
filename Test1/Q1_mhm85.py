# Question 1

# We need the os module to access the files
# We need the csv module to create a csv file
import os, csv

path = r"C:\Users\mhm85\Desktop\Question1"

in_files = os.listdir(path)

with open("Q1Output.csv", "w", newline = "") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["FileName", "EachFileAverage"])

    for filename in in_files:
        total = 0
        count = 0
        
        filepath = os.path.join(path, filename)
        file = open(filepath, "r")
        
        for line in file:
            total += int(line)
            count += 1

        file.close()

        average = total / count

        writer.writerow([filename, str(round(average, 2))])
