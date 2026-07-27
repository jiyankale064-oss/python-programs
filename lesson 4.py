print("===== Student Marks Calculator =======")

name = input("Enter Your Name")


math = int(input("Enter Math Marks: "))
science = int(input("Enter science Marks: "))
english = int(input("Enter english Marks: "))

total = math + science + english
percentage = total/ 3 

print("\n---- Result-----")
print("Students name", name)
print("total marks", total)
print("percentage", percentage)


print("\nComparison Results")
print("percentage >= 40",percentage >=40)
print("percentage <= 40",percentage <=40)

attendence = int(input("\nEnter attendence percentage: "))

eligible = (percentage >= 40) and (attendence >= 75)

print("Eligible to pass", eligible)


bonus = total
bonus += 5

print("Bonus Marks Added", bonus)

if eligible:
    print("\nCongratulations!",name,"You Have Passed" )
else:
    print("\nSorry",name,"you Have Failed")    

