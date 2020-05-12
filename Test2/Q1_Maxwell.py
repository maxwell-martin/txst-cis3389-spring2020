# Exam 2 - Question 1 - Maxwell Martin


# A list to hold month names.
months = [ 'January',
	   'February',
	   'March',
	   'April',
           'May',
	   'June',
	   'July',
	   'August',
	   'September',
	   'October',
	   'November',
           'December' ]

# List to hold monthly rainfall amounts.
rainfall = []

# Variable to hold total amount of rainfall for the year.
total = 0

# Request rainfall amounts for each month.
# Append amount entered by user to the list.
# Add amount entered by user to the total variable.
for month in range(1,13):
    entry = float(input("Enter rainfall amount for " + months[month - 1] \
                        + " (" + str(month) + "): "))
    rainfall.append(entry)
    total += entry

# Compute the average amount of rainfall for the year.
average = total / len(rainfall)

# Compute the maximum and minimum amounts of monthly rainfall for the year.
maximum = max(rainfall)
minimum = min(rainfall)

# Determine the month names for maximum and minimum monthly rainfall amounts.
max_month = months[rainfall.index(maximum)]
min_month = months[rainfall.index(minimum)]

# Write all values to a text file.
with open("Q1Output.txt", "w") as outfile:
    outfile.write("Total rainfall in Austin last year: " \
                  + format(total, ",.2f") + "\n")
    outfile.write("Average rainfall in Austin last year: " \
                  + format(average, ",.2f") + "\n")
    outfile.write("Maximum rainfall in Austin last year: " \
                  + format(maximum, ",.2f") + "\n")
    outfile.write("Minimum rainfall in Austin last year: " \
                  + format(minimum, ",.2f") + "\n")
    outfile.write("Month name with the maximum rainfall: " \
                  + max_month + "\n")
    outfile.write("Month name with the minimum rainfall: " \
                  + min_month + "\n")
    print("Data written to file.")
    
