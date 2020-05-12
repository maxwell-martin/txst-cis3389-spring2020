# Question 1


string = "Sam works in a company abc in New York. He joined the company last year 2019. Before joining ABC, he used to work for a small firm in Arizona. He worked there from 2015 to 2018. Before moving to Arizona Sam used to live in South Dakota and he has been living there since 2000's."


# a.
years = []
words = string.split()
for word in words:
    word.strip(".,")
    if word.isdigit():
        years.append(word)
    elif word[0:4].isdigit():
        years.append(word[0:4])
print("List of years mentioned in string:", years)



# b.
count_abc = string.lower().count("abc")
print("ABC (irrespective of case) appears", count_abc, "times.")

max_year = max(years)
print("Maximum year:", max_year)

min_year = min(years)
print("Minimum year:", min_year)



# c.
new_string = string.replace("h", "_")
new_string = new_string.replace("H", "_")
print(new_string)



# Print all outputs to a text file called “Q1Output.txt”.
with open("Q1Output.txt", "w") as outfile:

    # Write part a. to the file.
    aStr = "a. The list of years: "
    for year in years:
        aStr += (year + ", ")
    aStr = aStr.strip(" ,")
    outfile.write(aStr + "\n")

    # Write part b. to the file.
    bStr = "b. Count: " + str(count_abc) + \
        ", Maximum: " + max_year + ", Minimum: " + min_year
    outfile.write(bStr + "\n")

    # Write part c. to the file.
    cStr = "c. The new string: " + new_string
    outfile.write(cStr + "\n")
    
