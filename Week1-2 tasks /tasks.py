# Task 1 
age = 25
name = "Nodo"

print(age)
print(name)


#Task 2
length = 10.5
length2 = int(length)
print(length2)

#Task 3 
x, y, z = 5, 10.5, "Hello"
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

#Task 4
def greet(name):
    print(f"Hello {name}")

greet("Nodo")

#Task 5 
def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

# Task 6 
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}

for fruit in fruits:
    print(f"{fruit}  {fruit_colors[fruit]}")

# Task 7
list1 = [ a ** 2 for a in range(1,10)]
print(list1)

# Task 8 
for i in range(1, 20):
    if(i % 3 == 0):
        print(i)

# Task 9 
def fizz_buzz(n):
    for i in range(1,n):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)
fizz_buzz(20)

# Task 10 
def division(a,b):
    try:
        result = a / b 
    except ZeroDivisionError:
        print("Zero division isn't possible")

division(1,2)

# Task 11
def listIndex(list, index):
    try:
         print(list[index])
    except IndexError:
        print("Index is out of border")
listIndex([1,2,3,4],4)

# Task 12
def doubleInput():
    try:
        userNum = int(input("Write ur number "))
        print(userNum * userNum)
    except ValueError:
        print("You should Write number")
        doubleInput()

doubleInput()

# Task 13  - not working 
def hello():
    with open("hello.txt" "w") as file:
        file.write("Hello World")
        print("Successfully wrote 'Hello, World!' to hello.txt")

# Task 14 
def readHello():
    with open("hello.txt" "r") as file2:
        content = file2.read()
        print(content)

# Task 15 

