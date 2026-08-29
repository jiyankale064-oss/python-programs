name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_subject = input("Enter your favorite subject: ")
print("Name:", name, ", Age:", age, ", Favorite Subject:", fav_subject)

###################################################################################

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Error: Division by zero")

##########################################################################################


price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total_price = price * quantity
print("Total Price:", total_price)

############################################################

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

    ######################################################################

num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

############################################################        





fruits = ["apple", "banana", "mango", "orange", "grape"]
fruit = input("Enter a fruit: ").lower()
if fruit in fruits:
    print("Fruit exists in the list")
else:
    print("Fruit doesn't exist in the list")

#################################################################


password = input("Enter password: ")
if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

###################################################################

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "*", i, "=", num * i)
    i = i + 1
###############################################################


sentence = input("Enter a sentence: ")
print("Number of characters:", len(sentence))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())


###################################################################

numbers = []
for i in range(5):
    num = int(input("Enter number " + str(i+1) + ": "))
    numbers.append(num)

sum_val = 0
max_val = numbers[0]
min_val = numbers[0]
even_count = 0
odd_count = 0

for num in numbers:
    sum_val += num
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Sum:", sum_val)
print("Maximum:", max_val)
print("Minimum:", min_val)
print("Average:", sum_val / 5)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)