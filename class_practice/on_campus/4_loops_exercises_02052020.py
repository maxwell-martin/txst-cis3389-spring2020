# Loops exercises


# Print something 5 times
print('CIS 3389')
print('CIS 3389')
print('CIS 3389')
print('CIS 3389')
print('CIS 3389')


# While loop
i = 1
while i <= 5:
    print('CIS 3389')
    i = i + 1

i = 1
while i <= 10:
    print(i) # Print numbers from 1-10
    i = i + 1

i = 15
while i <= 20:
    print(i) # Print numbers from 15-20
    i = i + 1


# List and For loop
a = [1, 2, 'CIS3389', 'Computer', 345] # A list
print(a) # Prints the list
for i in a:   # Prints each value in the list
    print(i)


# Print numbers backward
i = 10
while i >= 5:
    print(i)
    i = i - 1


# range() function with for loops
for i in range(1, 6): # No step
    print(i)

for i in range(1, 11, 2): # Step by 2
    print(i)

for i in range(11): # Prints 0-10
    print(i)

for i in range(10, 1, -2): # Prints 10-1 stepping by 2 not including 1 at end
    print(i)

for i in range(1, 6):
    if i == 4:
        continue    # Continues to next iteration and does not print 4.
    print(i)
for i in range(11):
    print(i, end = ' ') # Prints value without newline character at end thus printing all on one line


# Exercise 1
i = 1
total1 = 0
while i <= 10:
    total1 += i
    i += 1
print(total1)

total2 = 0
for i in range(1, 11):
    total2 += i
print(total2)


# Exercise 2
total = 0
for i in range(11, 46, 2):
    total += i
print(total)


# Exercise 3
total = 0.0
for i in range (1, 6):
    value = float(input("Enter a number: "))
    total += value
print(total)


# Exercise 4
print("ft\tinches")
print("-------------")
for i in range(5, 11):
    feet = i
    inches = i * 12
    print(feet, "\t", inches)


# Exercise 5
SALES_TAX_PERCENTAGE = 0.014

subtotal = 0
tax = 0

choice = "yes"
while choice == "yes":
    value = float(input("Enter purchase amount to calculate tax: "))
    subtotal += value
    choice = input("Continue (yes/no)?: ").lower()
    while choice != "yes" or choice != "no":
        choice = input("Incorrect choice. Continue (yes/no)?: ").lower()
tax = subtotal * SALES_TAX_PERCENTAGE
print("Sales tax is: $", format(tax, ",.2f"), sep = "")


# Exercise 6
for i in range(2, 31):
    if i == 5 or i == 14 or i == 27:
        continue
    print(i)

