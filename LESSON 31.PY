subjects = ("Python", "Java", "HTML", "CSS", "JavaScript")

# Creating a tuple of mabks
marks = (85, 78, 92, 88, 95)

print("=======STUDENTS MARKS=====")

# Displaying complete tuples
print("Subjects:", subjects)
print("Marks:", marks)

# Accessing individual elements
print("\n========INDIVIDUAL MARKS======")

print("Python Marks:", marks[0])
print("Java Marks:", marks [1])
print("HTML Marks:", marks [2])
print("CSS Marks:", marks[3])
print("JavaScript Marks:", marks[4])

# Negative indexing
print("\n ========== NEGATIVE INDEXING=================")

print("Last subject:", subjects[-1])
print("Last marks:", marks[-1])

# Slicing
print("\n ==========SLICING==========")

print("First three subjects:", subjects[0:3])
print("First three marks:", marks[0:3])
print("Last two subjects:", subjects[-2:])
print("Last two marks:", marks[-2:])

# Length of tuple
print("\n ========== LENGTH===========")

print("Number of subjects:", len(subjects))
print("Number of marks:", len(marks))


print("\n ==========ALL SUBJECTS")

for subject in subjects:
  print(subject)

print("\n =========ALL MARKS======")

for mark in marks:
  print (mark)

# Display subject and marks together
print("\n ========== SUBJECT-WISE MARKS=============")

for i in range(len(subjects)):
  print(subjects[i], ":", marks[i])

# Finding total marks
total = sum(marks)

print("\nTotal Marks:", total)

# Finding average
average = total / len(marks)

print("Average Marks:", average)

# Highest and lowest marks
highest = max(marks)
lowest = min(marks)

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Finding position of highest mark
highest_position = marks.index(highest)

print("Highest Marks Subject:", subjects[highest_position])

# Membership operator
print("\n===========MEMBERSHIP=============")

if "Python" in subjects:
  print("Python is present in the subjects.")


if "C++" not in subjects:
  print("C++ is not present in the subjects.")

# Count function
print("\n ======COUNT FUNCTION====")

print("Number of times 85 appears:", marks.count(85))

# Index function
print("\n ========== INDEX FUNCTION======")

print("Position of HTML:", subjects.index("HTML"))

# Tuple concatenation
print("\n ======== TUPLE CONCATENATION========")

extra_subjects = ("SQL", "C++")

all_subjects = subjects + extra_subjects

print("Original Subjects:", subjects)
print("Extra Subjects:", extra_subjects)
print("All Subjects:", all_subjects)

# Tuple repetition
print("\n ========== TUPLE REPETITION==========")

small_tuple = ("Python",)

print("Original:", small_tuple)
print("Repeated:", small_tuple * 3)

# Nested tuple
print("\n=====NESTED TUPLE===========")


student = (
("Name", "Rahul"),
("Age", 15),
("Class", 10),
("Marks", marks)
)
print("Student Information:")

for item in student:
 print(item)

# Accessing nested tuple
print("\nStudent Name:", student[0] [1])
print("Student Age:", student[1][1])
print("Student Class:", student[2] [1])



print("\n===========TUPLE TO LIST")

marks_list = list(marks)

print("Original Tuple:", marks)
print("Converted List:", marks_list)

# Updating list
marks_list. append(90)

print("List after adding new marks:", marks_list)

# Converting list back to tuple
new_marks = tuple(marks_list)

print("Converted back to Tuple:", new_marks)


print("\n ==========FINAL REASULT=========")

print("Total Subjects:", len(subjects))
print("Total Marks:", total)
print("Average:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Top Subject:", subjects[highest_position])

