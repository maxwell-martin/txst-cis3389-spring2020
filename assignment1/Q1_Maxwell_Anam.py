# Q1

response = "yes"

while response == "yes":
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    num3 = int(input("Enter third integer: "))

    if (num1 == num2) or (num1 == num3) or (num2 == num3):
        print("One or more numbers is equal. Please enter 3 different numbers.")
    else:
        if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
            secondLargest = num1
        elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
            secondLargest = num2
        elif (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):
            secondLargest = num3

        average  = (num1 + num2 + num3) / 3

        print("The second largest number is: ", secondLargest)
        print("The average of the three numbers is: ", format(average, ",.2f"))

        response = input("Would you like enter more numbers (yes/no)? ").lower()

        while response != "yes" and response != "no":
            response = input("Please enter \"yes\" to continue or \"no\" to exit: ").lower()

    
