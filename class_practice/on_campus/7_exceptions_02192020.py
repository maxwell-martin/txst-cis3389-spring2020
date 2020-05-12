try:
    file = open("file.txt", "r")
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    print(a / b)
except ValueError as e:
    print("Wrong input,", e)
except ZeroDivisionError as e:
    print("Dividing by zero is not possible,", e)
except IOError as e:
    print("Error opening file,", e)
finally:
    if file != None:
        file.close()

print("done")
