lst = [1,3,5,6]

num = int(input("How many numbers: "))



for n in range(num):
    numbers = int(input("Enter Number"))
    lst.append(numbers)

print("Maximum element in the list is :" , max(lst) , "\n Minimum element in the list is :" , min(lst))