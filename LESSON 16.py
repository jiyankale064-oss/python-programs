print("====NUMBER STATISTICS PROGRAM========")

numbers = []
sum = 0
largest = 0 
smallest = 100
even_count = 0
odd_count = 0

for i in range(1,11):
    num = float(input("ENTER NUMBER [i]: "))

    sum = sum + num

if largest is None or num > largest:
    largest = num

if smallest is None or num > largest:
    smallest = num

if num % 2 ==0:
    even_count = even_count + 1

else:
    odd_count = odd_count + 1

average = sum / 10

print("/n========Result=======")
print(" ALL 10 NUMBERS:", numbers)
print("Sum:",sum)
print("AVERAGE:",average)
print("LARGEST NUMBER:", largest)
print("SMALLEST NUMBER:", smallest)
print("EVEN NUMBER COUNT:", even_count)
print("ODD NUMBER COUNT",odd_count)