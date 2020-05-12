# print() function and variables
print("Hello world!")
greet = "Hi"
greet = 5.9
print(greet)

num = 5.5
print(num)
print(type(num))
print('bye')

# input() function
#greet = input("Enter a greeting: ")
print(greet)

# int() function (casting)
#num = int(input("Enter a number: ")) # Converts string input to integer
print(1000/num)

# Math operators
num = 3 + 4 ** 2 - 1 / 3 # Add, exponent, subtract, float division
print(num)
num2 = 17 % 4 # Modulus (remainder); remainder is 1
print(num2)
num3 = 17 // 4 # Integer division; truncates positive
print(num3)
num4 = 17 // -2 # Integer division; rounds down negative
print(num4)

# print() function possibilities
print("Texas " + "State") # Concatenation
print("Texas", "State") # Concatenation
print("Texas\n" + "State") # Newline escape character
print("Texas\t\t" + "State") # Tab escape character
print("Texas", \ # Multi-line continuation character
      "State")
