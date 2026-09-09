#Python Program: All Important List Operations

numbers = [10, 20, 30, 20, 40]

print("Original List:", numbers)

# 1. len() - Number of elements
print("Length:", len(numbers))

# 2. max() - Largest element
print("Maximum:", max(numbers))

# 3. min() - Smallest element
print("Minimum:", min(numbers))

# 4. sum() - Sum of elements
print("Sum:", sum(numbers))

# 5. sorted() - Returns a sorted list
print("Sorted:", sorted(numbers))

# 6. list() - Converts something into a list
text = "Python"
letters = list(text)
print("String converted to list:", letters)

#

# 7. append() - Adds an element at the end
numbers . append (50)
print("After append:", numbers)

# 8. insert() - Adds an element at a particular position
numbers.insert(1, 15)
print("After insert:", numbers)

# 9. extend() - Adds multiple elements
numbers.extend([60, 70])
print("After extend:", numbers)

# 10. remove() - Removes a particular value
numbers.remove(20)
print("After remove:", numbers)

# 11. pop() - Removes an element
numbers.pop()
print("After pop:", numbers)

# 12. index() - Finds the position of an element
print("Index of 30:", numbers.index(30))

# 13. count() - Counts how many times an element occurs
print("Count of 20:", numbers.count(20))

# 14. sort() - Sorts the original list
numbers. sort()
print("After sort:", numbers)

# 15. reverse() - Reverses the original list
numbers.reverse()
print("After reverse:", numbers)

# 16. copy() - Creates a copy of the list
new_list = numbers.copy()
print("Copied list:", new_list)

new_list.clear()
print("After clear:", new_list)