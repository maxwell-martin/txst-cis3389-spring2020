# Question 2

'''

Possible Errors:

-If the user enters a non-integer value for year or divisor, a
    ValueError is thrown when parsing using int() function.

-If the user enters zero for the divisor, a ZeroDivisionError
    is thrown when using % (modulus) to check if leap year.

-If the user were to enter a number extremely large for the year, and
    extremely small for the divisor, an OverflowError could possibly
    occur. I handle this with a generic "except" at the end.

-Any other errors would be handled by the generic "except" at the end.

'''

try:
    invalidYear = True

    while invalidYear:
        # Non-integer would throw ValueError.
        year = int(input("Enter a year: "))

        if year > 0:
            invalidYear = False
        else:
            print("Invalid year. Must be greater than zero. Try again.")

    # Non-integer would throw ValueError.
    divisor = int(input("Enter number to divide the year value by: "))
    
    # If divisor == 0, a ZeroDivisionError is thrown.
    if year % divisor == 0 and divisor == 4:
        print(year, "is a leap year.")
    elif year % 4 == 0 and divisor != 4:
        print(year, "is a leap year (divisible by 4), but you did not enter 4 as the divisor.")
    else:
        print(year, "is not a leap year.")
    
        
except ValueError as valError:
    print("Please enter an integer for both year and divisor -",
          valError)

except ZeroDivisionError as zeroDivError:
    print("Division by zero is impossible. Please enter a divisor that is not zero -",
          zeroDivError)

except Exception as defaultError:
    print("Invalid input. Please try again -", defaultError)
    



