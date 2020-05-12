#--------------EXERCISE 1----------------
SALES_TAX_PERCENTAGE = 0.014
GROCERIES = 200.00
GAS = 25.00

subtotal = GROCERIES + GAS

print("John's subtotal is: $", format(subtotal, ",.2f"), sep="")

tax = subtotal * SALES_TAX_PERCENTAGE;

print("John's sales tax is: $", format(tax, ",.2f"), sep="")

groceries_other = float(input("Enter amount spent on groceries: "))
gas_other = float(input("Enter the amount spent on gas: "))

subtotal_other = groceries_other + gas_other

print("Your subtotal is: $", round(subtotal_other, 2), sep="")

tax_other = subtotal_other * SALES_TAX_PERCENTAGE

print("Your sales tax is: $", round(tax_other, 2), sep="")


#--------------EXERCISE 2----------------
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if n1 > n2:
    print("n1 is greater than n2")
elif n1 == n2:
    print("n1 is equal to n2")
else:
    print("n1 is less than n2")


#--------------EXERCISE 3----------------
SPEED = 60.0
DISTANCE = 350.0
TIME = 4.0

distance_after_4_hours = SPEED * TIME
print("Distance traveled after 4 hours:", round(distance_after_4_hours, 2))

distance_remaining_after_4_hours = DISTANCE - distance_after_4_hours
print("Distance remaining after 4 hours:", round(distance_remaining_after_4_hours, 2))


#--------------EXERCISE 4----------------
a = int(input("Enter a number: "))
if a > 0:
    print("a is positive")
elif a < 0:
    print("a is negative")
else:
    print("a is zero")


#--------------Extra Exercise - Determine if even, odd, or zero----------------
b = float(input("Enter a number: "))
if b == 0:
    print("b is zero.")
elif b % 2 == 0:
    print("b is even.")
else:
    print("b is odd.")


#--------------EXERCISE 5----------------
answer = input("Is Python open source? ")
if answer.lower() == "yes":
    print("You are correct")
elif answer.lower() == "no":
    print("Your answer is wrong")
else:
    print("You entered a garbage value.")


#--------------EXERCISE 6 and 7----------------
day = int(input("Enter a number for the day of the week (1-7): "))
if day >= 1 and day <= 7:
    if day == 1:
        print("Sunday")
    elif day == 2:
        print("Monday")
    elif day == 3:
        print("Tuesday")
    elif day == 4:
        print("Wednesday")
    elif day == 5:
        print("Thursday")
    elif day == 6:
        print("Friday")
    else:
        print("Saturday")
else:
    print("Day entered is not between 1-7. Please try again.")


#--------------EXERCISE 8 and 9----------------
grade1 = float(input("Enter value for grade 1: "))
grade2 = float(input("Enter value for grade 2: "))

if grade1 <= 50 and grade1 >= 0 and grade2 <= 50 and grade2 >= 0:
    total_grade = grade1 + grade2
    if total_grade >= 65:
        if total_grade >= 90:
            print("Grade: A")
        elif total_grade >= 80:
            print("Grade: B")
        elif total_grade >= 70:
            print("Grade: C")
        else:
            print("Grade: D")
    else:
        print("Failing grade")
else:
    if grade1 > 50 or grade1 < 0:
        print("Grade 1 cannot be greater than 50 or less than zero.")
    if grade2 > 50 or grade2 < 0:
        print("Grade 2 cannot be greater than 50 or less than zero.")
    
    
