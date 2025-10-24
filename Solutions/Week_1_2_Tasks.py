# Task1
print("\nTask1")
age = 25
name = "Daviti"
print(f"{name} is {age} years old.")

# Task2
print("\nTask2")
length = 10.5
int_length = int(length)
print(f"length is {length},\nint_length is {int_length}")

# Task3
print("\nTask3")
x, y, z = 5, 0.5, "hello"
print("x:{}, y:{}, z:{}".format(x,y,z)) 

# Task4
print("\nTask4")
def greet(name):
    return f"Hello, {name}"
print(greet("dato"))

# Task5
print("\nTask5")
def is_even(num):
    return True if num % 2 == 0 else False
print(is_even(4))
print(is_even(7))

# Task6
print("\nTask6")
fruits = ["apple","banana","orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}
for fruit in fruits:
    print(f'{fruit} color is {fruit_colors.get(fruit)},\n')

# Task7
print("\nTask7")
numbers_in_square = [number ** 2 for number in range (1,10)]
print(numbers_in_square)

# Task8
print("\nTask8")
print([number for number in range(1,20) if number % 3 == 0])

# Task9
print("\nTask9")
def fizz_buzz(n):
    for number in range(1, n):
        if number % 5 == 0: 
            if number % 3 == 0: 
                print("FizzBuzz") 
            else:
                print("Buzz") 
        elif number % 3 == 0:
            print("Fizz") 
        else:
            print(str(number))
print(fizz_buzz(20))

# Task10
print("\nTask10")
def dev(n, m):
    return n / m

#here is the wrong division to trigger the except part
try:
    print(dev(10, 0))
except ZeroDivisionError:
    print("-go learn math.")
    
#here is correct division to pass try part
try:
    print(dev(10, 5))
except ZeroDivisionError:
    print("go learn math.")

#  Task11
print("\nTask11")
def get_value(list, index):
    return list[index]

#here is the wrong indexing to trigger the except part
try:
    print(get_value(["a","b","c","d"], 4))
except IndexError:
    print("-you are wwaayy out of range")

#here is correct indexing to pass try part
try:
    print(get_value(["a","b","c","d"], 3))
except IndexError:
    print("-you are wwaayy out of range")

# Task12
print("\nTask12")
while True:
    try:
        print(int(input("+Type the number->")) ** 2)
        break
    except ValueError:
        print("-Pass the number as an input!")

# Task13
print("\nTask13")
with open("hello.txt", "w") as file:
    file.write("Hello, World!")
print("+file with context successfuly created")

# Task14
print("\nTask14")
try:
    with open("hello.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("-First create file and then you can read it.")

# Task15
print("\nTask15")
def reading_numbers():
    try:
        print("Reading the numbers...")
        with open("numbers.txt", 'r') as file:
            numbers = [int(number.strip()) for number in file.readlines()]
            print("This is the sum of the numbers in a file-> {}".format(sum(numbers)))
            print("This is the mean of the numbers in a file-> {}".format(sum(numbers)/len(numbers)))
    except FileNotFoundError:
        print("Kaboom! You have no file!\nOkay let me create it for you...")
        with open("numbers.txt", "w") as file:
            file.writelines([f"{number}\n" for number in range(1,100)])
        print("Creating Done!")
        reading_numbers()
    except ValueError:
        print("Kaboom! You have banana(non-integer-value) in numbers.txt, correct it and then run the program again!")
    except ZeroDivisionError:
        print("Kaboom! file is empty!")
reading_numbers()