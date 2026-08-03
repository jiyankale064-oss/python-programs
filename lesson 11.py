print("=====STRING OPERATIONS=======")

# Input
text = input("Enter a sentence: ")

print("\nOriginal String :", text)

# Length
print("\n1. Length :", len(text))

# Upper and Lower
print("2. Uppercase :", text.upper())
print("3. Lowercase :", text. lower())

# Title and Capitalize
print("4. Title Case :", text.title())
print("5. Capitalize :", text.capitalize())

# Swap Case
print("6. Swap Case :", text.swapcase())

# Replace
old = input("\nEnter word to replace: ")
new = input("Enter new word: ")
print("10. Replace :", text.replace(old, new))

# Count
ch = input("\nEnter character to count: ")
print("11. Count :", text.count(ch))

# Find
word = input("\nEnter word to find:")
print("12. Find :", text.find(word))

# Startswith & Endswith
start = input("\nEnter starting word: ")
end = input("Enter ending word: ")

print("13. Starts With :", text.startswith(start))
print("14. Ends With :", text.endswith(end))

# Membership Operator
search = input("\nEnter word to search: ")

if search in text:
    print("15.", search, "is present.")
else:
    print("15.", search, "is not present.")

# String Comparison
another = input("\nEnter another string for comparison: ")

if text == another:
   print("16. Both strings are Equal")
else:
   print("16. Both strings are Not Equal")

# Slicing
print("\n17. First 5 Characters :", text[:5])
print("18. Last 5 Characters :", text[-5:])
print("19. Reverse String :", text[ ::- 1])

# Indexing
print("20. First Character :", text[0])
print("21. Last Character :", text[-1])

# Split
words = text.split()
print("22. Split :", words)

# Join
joined = "-".join(words)
print("23. Join :", joined)

# Alphabet, Digit, Alphanumeric
print("\n24. Is Alphabet :", text.isalpha())
print("25. Is Digit :", text.isdigit())
print("26. Is Alphanumeric :", text.isalnum())

# Lower, Upper, Title Checks
print("27. Is Lower :", text.islower())
print("28. Is Upper :", text.isupper())
print("29. Is Title :", text.istitle())

# Space Check
print("30. Is Space :", text.isspace())

# Center, Left Justify, Right Justify
print("\n31. Center :", text.center(50, "*"))
print("32. Left Justify :", text.ljust(50, "-"))
print("33. Right Justify :", text.rjust(50, "-"))