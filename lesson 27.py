# Python Program on Tuples

# Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("Tuple:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("First three fruits:", fruits[0:3])

# Length of tuple
print("Number of fruits:", len(fruits))

# Checking an item
if "Mango" in fruits:
   print("Mango is present in the tuple")

# Counting an item
numbers = (10, 20, 10, 30, 10, 40)

print("Numbers:", numbers)
print("Number of times 10 occurs:", numbers.count(10))

# Finding the position of an item
print("Position of 30:", numbers.index(30))

# Looping through a tuple
print("All fruits:")
for fruit in fruits:
   print(fruit)