tuple1 = (2,3,5,6)
print(tuple1[0])

# Check type of variable
print(type(tuple1)) # A tuple

# Check type of variable
aTuple = (2)
print(type(aTuple)) # An int

# Create a tuple with one element
aTuple2 = (2,)
print(type(aTuple2)) # A tuple

a,b,c,d = tuple1
print(b)

# Cannot change values in tuple
# tuple1[2] = 4

# Convert tuple to list
list1 = list(tuple1)
print(list1)

# Convert list to tuple
tuple2 = tuple(list1)
print(tuple1)

# Add two tuples
tup1 = (2,3,4)
tup2 = (5,6,7)
print(tup1 + tup2)


# Exercise 3
tuple3 = (1,2,7,5,4,3,'s','r',4,8)
list1 = list(tuple3)
removed_items = [5,4,3]
for i in removed_items:
    list1.remove(i)
print(list1)
print(tuple(list1))
# OR
tup1 = (1,2,7,5,4,3,'s','r',4,8)
t1 = tup1[:3]
t2 = tup1[6:]
print(t1 + t2)


# Exercise 4
a = [[2,3,4,6], [1,2], [7,7,10]]

total = 0
# Element-wise summation
for i in a: 
    for j in i:
        total += j
print("Total:", total)

total = 0
# Index-wise summation
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        total += a[i][j]
print("Total:", total)


# Exercise 5
def main():
    sales = []
    day_names = ["Sunday", "Monday", "Tuesday"]
    for i in range(3):
        sales.append(float(input("Enter sales for day " + str(i + 1) + ": ")))
    t_sales = total_sales(sales)
    m_sales = max_sales(sales)
    day = day_names[sales.index(m_sales)]
    print("Total sales:", t_sales)
    print("Max sales:", m_sales)
    print("Day of max sales:", day)
    
def total_sales(lst):
    return sum(lst)

def max_sales(lst):
    return max(lst)

main()


# Exercise 6
def main():
    valid = False
    
    while not valid:
        num = int(input("Enter an integer greater than 1: "))
        if num > 1:
            valid = True
            
    lst = []
    
    for i in range(1, num + 1):
        lst.append(i)
    print(lst)
    
    for j in lst:
        status = even_or_odd(j)
        print(j, ":", status)

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

main()
