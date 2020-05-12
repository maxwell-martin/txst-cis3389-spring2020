items = ["Milk", "Egg", "Oil", "Butter"]

print(items)
print(items[0]) # Milk

print(items[3]) # Last item: Butter
print(items[-1]) # Last item: Butter

print(len(items)) # Use len() function to get length of list

items[1] = "Bread" # Change Egg to Bread; second index
print(items)

items.append("Cookies") # Use append() function to add item to list
print(items)

items.insert(2, "Strawberry") # Inserts value in 2 index; Oil to Strawberry
print(items)

items.remove("Oil") # Removes Oil for them list
print(items)

items.pop() # Use pop() function to remove last item in list
print(items)

items.pop(1) # Use pop() function to remove item 1 index; Removes Bread
print(items)

del items[1] # Use del keyword to delete item at 1 index; Removes Strawberry
print(items)

print(items.index("Milk")) # Use index() function to get index of item

for i in items:
    print(i)

items = ["Milk", "egg", "Oil", "butter"]
items.sort(key = str.lower) # Sort string list by lowercase value in alphabetical order
print(items)
items.sort(key = str.lower, reverse = True) # Sort string list by lowercase value in reverse alphabetical order
print(items)

# Count how many times a value exists in list
number_list = [2, 3, 4, 16, 18, 4, 20, 24]
count = number_list.count(4)
print(count)

print(number_list.index(4)) # Gives first index where value 4 appears in list

print(sum(number_list)) # Get sum of all numbers in list

print(min(number_list)) # Get smallest number in list

print(max(number_list)) # Get largest number in list

number_list.reverse() # Reverse order of numbers in list
print(number_list)

number_list.reverse()
print(number_list[3:]) # Get all values from index 3 onward

print(number_list[2:5]) # Get 4, 16, and 18 only, index 2 inclusive to 5 exclusive


# Example 1
def greater_less(lst, num):
    greater_than_list = []
    less_than_list = []

    for i in lst:
        if i > num:
            greater_than_list.append(i)
        else:
            less_than_list.append(i)

    return greater_than_list, less_than_list
    

def main():
    number = 20
    numbers = [2, 5,20,45,50,7,10,67]

    # Return to two variables
    #greaterlist, lesslist = greater_less(numbers, number)
    #print("Greater than list:", greaterlist)
    #print("Less than list:", lesslist)

    # Use index of tuple instead
    result = greater_less(numbers, number)
    print("Greater than list:", result[0])
    print("Less than list:", result[1])

main()


# Example 2
import math

lst = []

for i in range(1, 21):
    lst.append(round(math.sqrt(i), 2))

print(lst)
print(lst[4:18])


# Example 3
numbers = [5,5,6,7,5,8,9,6,8,9,4,0,4,4]


# With module
import collections
print(collections.Counter(numbers))

# Without module
counts = []
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
        counts.append(numbers.count(i))
print(unique)
print(counts)


# Example 4
x = 20
y = 20
try:
    z = int(input("Enter an integer: "))
    result = x + y / z
    print("The result of", x, "+", y, "/", z, "=", round(result, 2))
except ValueError as e:
    print("Please enter an integer", "|", "Error:", e)
except ZeroDivisionError as e:
    print("Diving by zero is impossible.",
          "Please enter an integer other than zero.", "|", "Error:", e)
except Exception as e:
    print("Error:", e)
        

# Demo of 2D list
exam_score = [["John", 67, 89, 56],
              ["Bill", 45, 80, 56],
              ["Ana", 89, 78, 60]]

print(exam_score)

# Print each element in 2D list
for i in exam_score:
    for j in i:
        print(j)

# Add new item to exam_score list the long way
score_4 = []
score_4.append("Nancy")
score_4.append(67)
score_4.append(90)
score_4.append(77)
print(score_4)
exam_score.append(score_4)
print(exam_score)

# Add new item to exam_score the short way
exam_score.append(["Harold", 50, 100, 80])
print(exam_score)

# Two dimensional list
a = [[1,2,3], [3,4,-5], [5,6,7]]
print(a[0][1]) # Prints 2
print(a[2][0]) # Prints 5
