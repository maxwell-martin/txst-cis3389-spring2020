# Q2

print("a. Number\tb. Square")

sumOfSquares = 0

for i in range(5, 31):
    if i != 10 and i != 15 and i % 5 == 0:
        square = i ** 2
        sumOfSquares += square
        print("  ", i, "\t\t  ", square)

print("c. Sum of squares:", sumOfSquares)
