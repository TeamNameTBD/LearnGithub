# Python Variables

# Declare using =
var_a = 5

# Data Types
# string        - Text Field
var_b = "Hello"
# int           - Integer
var_c = 2
# float         - Floating Point Value
var_d = 1.1234
# list          - A list of items, can be mixed types. Indicated wit []
var_e = [1, 1.2, "Hello", var_c]
# tuple         - Similar to a list, but takes up less space and cannot be changed. Indicated with ()
var_f = (25, 50)
# dictionary    - A group of values that can be called using keys. Indicated by {}
var_g = {"value 1": 1, "value 2": 2.5, "value 3": 5}

# Update variables
# Int and float
# Use math on variables ( +, -, *, /, %)
print(var_a + 5)
print(var_a * 3)

# save value
var_a = var_a + 1
# alternative syntax
var_a += 1

# String
s1 = "Hello"
s2 = "World"
# append strings with +
s3 = s1 + " " + s2

# List
# get a value from a list
# The first Item is in position 0
l1 = [0, 1, 2, 3]
print(l1[0])
print(l1[1])
# You can count backwards too
print(l1[-1])
# Add an item to a list
l1.append(4)
# Sort a list
l1.sort()
# Remove an item
l1.pop(0)
print(l1)

# Tuples
# Most often used for displaying coordinates or other static data
coords = (50, 75)

# Dictionary
# Add custom keys and values
dict1 = {
    "Andrew": "Texas",
    "Devin": "Washington",
    "Jonathan": "Colorado"
}
# Call a value
print(dict1["Andrew"])
# Add a value
dict1["Chris"] = "Tennessee"
# Remove a value
dict1.pop("Chris")
# Loop through all values
for key, value in dict1.items():
    print(key, value)
