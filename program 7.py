"""
CAR GAME
>help
start = to start the car
stop = to stop the car
quit = to exit

>asd
i don't understand this
>start
car started , ready to go
>stop
car stopped
"""

#for loop
for i in [1,2,34]:
    print(i)
for i in range(10):
    print(i)
for i in range(2,12):
    print(i)
for i in range(2,20,3):
    print(i)

#total cost of all prices in shopping
prices = [12 , 33 , 32 , 54 , 34]
total = 0
for price in prices:
    total+=price   # total = total + price
print(f"total : {total}")

#Nested loops
#make list of coordinates
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

#CHALLENGE
list = [9,2,2,7,2,2,2]
for i in list:
    print("x" * i)
list1 = [2,2,2,2,7,7]
for m in list1:
    print("+" * m)

list = [5,2,5,2,2]
for x_count in list:
    output = ""
    for count in range(x_count):
        output+='x'
    print(output)


#lists
names = ["john" , "sarah" , "mary"]
print(names)
print(names[0])
print(names[2])


#write a program to find the largest number in a list
list = [1,3,9,23,67,43,78,32,12]
max = list[0]
for i in list:
    if i > max:
        max = i
print(max)

#2D list
#most powerul in data science and machine learning

Matrix = [
    [2,3,4],
    [4,5,6],
    [7,1,9]
]
for row in Matrix:
    for item in row:
        print(item)
print(Matrix[2][1])


#list methods
numbers = [2,3,6,8,65]
numbers.append(34)
print(numbers)
numbers.insert(2,78)
print(numbers)
numbers.copy()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(34))
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)

numbers.clear()
print(numbers)
numbers.append(34)
print(numbers)
numbers.insert(2,34)
print(numbers)
print(numbers.count(34))
numbers.insert(5,23)
numbers.insert(4,98)
numbers.insert(8,45)
numbers.insert(1,32)
numbers.insert(9,56)
print(numbers)
print(numbers.index(34))
print(numbers.index(56))
print(numbers.index(98))
print(56 in numbers)
print(34 in numbers)
print(11 in numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#write a program to remove a duplicate in a list
dup_list = [23,56,54,34,67,23,55,45,54,23,67]
new_list = []
for i in dup_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)


#tuple
number = (2,4,6)
print(number.count(4))
print(number.index(6))
print(number)

#unboxing
coordinates = (1,2,3)
print(coordinates[0] * coordinates[1] * coordinates[2])
x  = coordinates[0]
y  = coordinates[1]
z  = coordinates[2]
print(x*y*z)


