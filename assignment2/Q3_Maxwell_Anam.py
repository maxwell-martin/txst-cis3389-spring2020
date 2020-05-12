# Question 3


a = {5:'New York',2: 'Dallas', 6: 'San Marcos'}
b = {2: 'Texas', 4: 'San Francisco'}
c = {3: 'Phoenix', 1: 'Arizona'}


# Concatenate the dictionaries into a new dictionary.
# 2 is the key for two different values, which is not allowed in a dictionary.
# Thus, Python overwrites key-value pair 2:'Dallas' with 2:'Texas'
d = {}
d.update(a)
d.update(b)
d.update(c)
print(d)


# The "second element value" from the new dictionary.
# Dictionaries do not have indexing like lists, so there really is no
# such thing as a "second element". I am assuming "second element value" is the
# value associated with key = "2".
print(d[2])
# If my assumption is incorrect, here is the second element from the list of
# values in the dictionary. Coincidentally, it is the same as above.
values = list(d.values())
print(values[1])


# Print dictionary with keys sorted in descending order
for key in sorted(d.keys(), reverse = True):
    print(key, "::", d[key])
