#python program: differnt string operations

text = input("Enter a string: ")

print("\n------String Operations------")

print("Length:", len(text))

print("Uppercase:", text.upper())

print("Lowercase:", text.lower())


print("Capitalized:", text.capitalize())


ch = input("Enter a character to count: ")
print("Count of", ch, ":", text.count(ch))


search = input("ENTER A CHARACTER/WORD TO FIND: ")
print("position:", text.find(search))

old = input("Enter word to replace: ")
new = input("Enter a New word: ")
print("After replacement:", text.replace(old,new))

start = input("Enter starting Text: ")
print("Starts with", start, ":", text.startswith(start))

end = input("Enter ending Text: ")
print("Ends with", end, ":", text.endswith(end))

print("Reversed:" , text[::-1])
