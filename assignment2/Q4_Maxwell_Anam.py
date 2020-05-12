# Question 4


import os, csv

path = r"C:\Users\maxma\Desktop\college_pcfd\spring_2020\CIS3389.251_Python\assignments\assignment2\Q4"

files = os.listdir(path)

with open("Q4Output.csv", "w", newline = "") as outfile:
    writer = csv.writer(outfile, delimiter = "\t")
    writer.writerow(["FileName", "Substring"])
    for filename in files:
        filepath = os.path.join(path, filename)
        file = open(filepath)
        sentences = file.read().split(".")
        for sentence in sentences:
            sentence = sentence.strip()
            if "lives" in sentence:
                partitions = sentence.partition("lives")
                writer.writerow([filename, partitions[2] + "."])
            elif "live" in sentence:
                partitions = sentence.partition("live")
                writer.writerow([filename, partitions[2] + "."])
        file.close()
                

# The format described in the instructions appears to suggest that the separation
# of the "FileName" and "Substring" should be TAB (\t) delimited. If you open up
# the "Q4Output.csv" in Excel, Excel does not show the tab delimitation. However,
# the tab delimitation is there and is viewable when the file is opened in a text
# editor.
