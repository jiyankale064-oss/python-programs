print("=======STUDENTS MARKS ANALYZER=======")

name = input("ENTER STUDENTS NAME")
subjects = int(input("ENTER NUMBER OF SUBJECTS"))

total = 0
highest = 0
lowest = 100
passed = True

for i in range(1, subjects + 1):
    marks = float(input("ENTER MARKS FOR SUBJECT " + str(i) + ": "))

    total = total + marks

    if marks > highest:
        highest = marks

    if marks < lowest:
            lowest = marks   

    if marks < 35:
        passed = False

average = total / subjects     

print("\n ===== RESULT=====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

if passed:
     print(" REASULT CHILD HAS PASSED")
else:
     print("REASULT CHILD HAS FAILED") 

if average >= 90:
   grade = "A+"
elif average >= 80:
   grade = "A"
elif average >= 70:
   grade = "B"
elif average >= 60:
   grade = "C"
elif average >= 50:
   grade = "D"
else:
   grade = "F"

print("Grade:", grade)         