a = 10
b = 5

# Condition structure
if a < b:
    print("a is less")
else:
    print("a is not less")

c = 7

if a < b:
    print("a is less")
else:
    if c < b:
        print("c is less")

for i in range(5): # Range from 0 - 4; does not include 5
    print(i ** 2)

score = float(input("Enter a score: "))
print("Score =", score)

# Nested if statments
if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

# Elif if statments
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Cannot concatenate string and numeric type with  "+"
#print("Test " + 1.0)

# Can concatenate string and numeric type with ","
#print("Test", 1.0)

a = 5
b = 10
c = 15

# Or operator
if (a == 5 or b == 10 or c == 100):
    print("Ok")
else:
    print("Not ok")

# And and Not operators
if (a == 5 and b == 10 and c == 100):
    print("Ok")
else:
    print("Not ok")

# Boolean variables
x = a < b   # Assigning result of condition (T/F) to variable
y = False

if x:               # Same as x == True
    print("x")
else:
    print("not")

if not x:           # Same as x != True
    print("x")
else:
    print("not")
