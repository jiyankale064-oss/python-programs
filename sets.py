python_students = {"Aarav" , "Riya", "Kabir", "Anaya", "Vihaan"}
java_students = {"Riya", "Kabir" , "Ishaan", "Meera", "Anaya"}



print("Python Students:", python_students)
print("Java Students:", java_students)


#ADD 
python_students.add("Arjun")
print("\nAfter adding Arjun:", python_students)


#UPDATE
java_students.update(["Sara", "Dev"])
print("After adding students:", java_students)


#REMOVE
python_students.remove("Vihaan")
print("\nAfter removing Vihaan:", python_students)


#DISCARD
java_students.discard("Rahul")
print("After discarding Rahul:", java_students)


#UNION
all_students = python_students.union(java_students)
print("\nAll Students:", all_students)


#INTERSECTION
common_students = python_students.intersection(java_students)
print("Students learning both:", common_students)

 
#DIFFERENCE
only_python = python_students.difference(java_students)
print("Only Python Students:", only_python)

#DIFFERENCE
only_java = java_students.difference(python_students)
print("Only Java Students:", only_java)


#SYMETRIC DIFF
different_students = python_students.symmetric_difference(java_students)
print("Students learning only one course:", different_students)


#CHECKING MEMBERSHIP
if "Riya" in python_students:
        print("\nRiya is enrolled in Python")


#FIND TOTAL STUDENTS
print("\nTotal Python Students:", len(python_students))
print("Total Java Students:", len(java_students))
print("Total Unique Students:", len(all_students))


# 12. Displaying students using a loop
print("\nList of All Students:")

for student in all_students:
   print(student)

# 13. Checking subset
if common_students.issubset(all_students):
   print("\nCommon students are part of all students.")

# 14. Checking superset
if all_students.issuperset(python_students):
   print("All students include every Python student.")

print("\nCourse Management Completed!")