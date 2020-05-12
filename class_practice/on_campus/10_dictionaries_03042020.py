# Dictionaries

# Create a dictionary
Dic1 = { 1:34, 2:45, 3:89 }
print(Dic1)

# Get value from dictionary
print(Dic1[2])
print(Dic1.get(2))

# Error thrown when key does not exist
#print(Dic1[4])

# No error thrown when key does not exist; returns None instead
print(Dic1.get(4))
print(Dic1.get(4, "Default message"))

# Calculate number of elements in dictionary
print(len(Dic1))

# Add key value pair to dictionary
Dic1[4] = 67
print(Dic1)

# Change value of a kvp
Dic1[3] = 100
print(Dic1)

# Delete kvp from dictionary
#del Dic1[3]
#print(Dic1)

# Delete all key value pairs from dictionary
#Dic1.clear()
#print(Dic1)

# Keys() method
for key in Dic1.keys():
    print(key)
for key in Dic1: # Does the same thing as Dic1.keys()
    print(key)

# Values() method
for value in Dic1.values():
    print(value)

# Items() method
for i in Dic1.items():
    print(i)

# Pop() method
#Dic1.pop(2)
#print(Dic1)

# Popitem() method
Dic1.popitem()
print(Dic1)


# Exercise 7
##school = { "CIS3389":["Aindrila Chakraborty", 40],
##           "CIS3380":["Kevin Jetton", 120],
##           "CIS3325":["Mayur Mehta", 30] }
##course_num = input("Enter a course number: ")
##if course_num in school.keys():
##    print(school.get(course_num)[0], "-", school.get(course_num)[1])
##else:
##    print(course_num, "is not a course.")


# Exercise 8
school = { "CIS3389":["Aindrila Chakraborty", 40],
           "CIS3380":["Kevin Jetton", 120],
           "CIS3325":["Mayur Mehta", 30] }
for key in school.keys():
    print(key, ";", school[key])
 #OR
for k, v in school.items():
    print(k, ";", v)


# Exercise 9 - Sort dictionary
Dic2 = { 1:34, 3:45, 2:89 }
for key in sorted(Dic2.keys()):
    print(key)
for key in sorted(Dic2.keys(), reverse = True):
    print(key)


# Exercise 10
dic1={1:10, 2:20}
dic2={3:'texas', 4:'mexico'}
dic3={5:'ny',6:'45'}
dic4 = {}
for dic in (dic1, dic2, dic3):
    dic4.update(dic)
print(dic4)


# Exercise 11
matrix = [["NY", "New York"], ["CA", "California"], ["TX", "Texas"]]
dict5 = dict(matrix)
print(dict5)
