# Task 1
age = 25
name = "Mariam"
print(age)
print(name)

# Task 2
length = 10.5
int_length = int(length)
print(length, int_length)

# Task 3
x = 5
y = 10.5
z = 'Hello'
print(f"x: {x}, y: {y}, z: {z}")

# Task 4
def greet(name):
    return "Hello, " + name + "!"

print(greet("Mariam"))

# Task 5
def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))

# Task 6
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}
for i in fruits:
    print(i , fruit_colors[i])
    

# Task 7
lst = [x ** 2 for x in range(1, 11)]
print(lst)

# Task 8
for i in range(1, 21):
    if i % 3 == 0:
        print(i)
        
        
# Task 9
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0: 
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(20)

        
fizzbuzz(20)

# Task 10
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero encountered!"
    
print(div(2, 4), div(1, 0))

# Task 11
def func(lst, n):
    try:
        return lst[n]
    except IndexError:
        return "Index is out of bounds!"
    
print(func([1,2], 1))
print(func([1,2,], 4))

# Task 12
def square():
    txt = input("Write a number: ")
    try:
        print(int(txt) ** 2)
    except ValueError:
        square()
        
# Task 13
with open("hello.txt", "w") as f:
    f.write("Hello, world!")
    print("success!")
    
    
# Task 14    
try:
    with open("hello.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File 'hello.txt' does not exist!")
    
    
# Task 15
with open("numbers.txt", "w") as f:
    f.write("10\n20\n30\n40\n50\n")

with open("numbers.txt", "r") as f:
    lines = f.readlines()
    numbers = []

    for line in lines:
        line = line.strip()
        if line:
            numbers.append(float(line))

    sum1 = sum(numbers)
    avg = sum1 / len(numbers) if len(numbers) != 0 else None

    print("Sum:", sum1)
    print("Average:", avg)


