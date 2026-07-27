print("=======EMPLOYEES SALARY CALCULATOR=========")

name = input("Enter Your Name")
basic_salary = float(input("Enter your basic salary: "))
bonus = float(input("Enter your bonus: "))
tax_amount = float(input("  Enter your Tax amount:"))
years_of_experience = int(input("Enter years of Experience: "))

gross_salary =  basic_salary + bonus
net_salary = gross_salary - tax_amount

print("\n-----------Salary Slip----------")
print("Employee Name", name)
print("Gross salary", gross_salary)
print("Net Salary", net_salary)

print("\n--------Salary Check---------")
print("Net salary >= 50000",net_salary >= 50000)
print("Net salary <= 50000",net_salary <= 50000)

print("\n------Promotion Eligibility Check-------")
is_eligible =  (net_salary >= 30000) and (years_of_experience >= 2)

print("\n----Promotion Status-------")
if is_eligible:
  print ("\nCongratulations",name," is eligible for promotion.",)
else: 
  print("\nSorry!,name, is not eligible for promotion.",)    