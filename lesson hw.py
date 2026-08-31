# Get user input
name = input("Enter a string: ")

# String slicing operations
print("First 5 characters:", s[:5])
print("Last 5 characters:", s[-5:])
print("Characters from index 2 to 7:", s[2:8]) 
print("Every second character:", s[::2])
print("String in reverse order:", s[::-1])

################################################33

# Find the space between first and last name
space = name.index(" ")

first_name = name[:space]
last_name = name[space + 1:]

print("First name:", first_name)
print("Last name:", last_name)
print("First 3 characters:", name[:3])
print("Last 3 characters:", name[-3:])
print("Reverse of full name:", name[::-1])