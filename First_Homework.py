#Task1
age = 21
name = "Jane"
print(age)
print(name)

#Task2
length = 10.5
int_length = int(length)
print(length)
print(int_length)

#Task3
x = 5
y = 10.5
z = "Hello"
print(f"x:{x}, y:{y}, z:{z}")

#Task4
def my_greeting_function(name):
    return (f"Hello, {name}")
print(my_greeting_function("Tekla"))

#Task5
def is_even(num):
    return True if num % 2 == 0 else False
print(is_even(5))

#Task6
fruits = ["apple", "banana", "cherry"]
fruit_colors = {"apple" : "green", "banana":"yellow", "cherry" : "red"}

for fruit in fruits:
    color = fruit_colors[fruit]
    print(f"fruit: {fruit}, color: {color}")

humans = ["tekla", "keso", "lizi"]
heights = {"tekla":"maghali", "keso": "sashualo", "lizi" : "dabali"}
for human in humans:
  height = heights[human]
  print(f"human: {human}, height: {height}")

seasons = ["Spring", "Summer", "Autumn", "Winter"]
holidays = {"Spring":"Easter", "Summer": "vacation", "Autumn": "Halloween", "Winter": "Christmas"}
for season in seasons:
    holiday = holidays[season]
    print(f"season: {season}, holiday: {holiday}")
#task 7
Squares = [x**2 for x in range(1,11)]
print(Squares)

word = "tekla"
up = [char.upper() for char in word ]
print(up)

#task8
nums = range(1,21)
divisible_by_three = [num for num in nums if num % 3 == 0]
print(divisible_by_three)

#task9

def fizz_buzz(ricxvi):
    if ricxvi % 3 == 0 and ricxvi % 5 == 0:
        print("FizzBuzz")
    elif ricxvi % 3 == 0:
        print("Fizz")
    elif ricxvi % 5 == 0:
        print("Buzz")
    else:
        print(ricxvi)

fizz_buzz(20)

#task10

def division(num1, num2):
    try:
        result= num1/num2
    except ZeroDivisionError:
        print("Error: You can not divide by zero")
    else:
        return result

res= division(10, 20)

print(res)


#task11
def get_value_at_specific_index(list, index):
    try:
        return list[index]
    except IndexError:
        print(f"ERROR: Index {index} is out of range")
        return None

print(get_value_at_specific_index([1,2,3,4,5], 3))

#task12
def int_squares():

    while True:
        try:
            user_input = input("Enter a number: ")
            number = int(user_input)**2
            return number
        except ValueError:
            print(f"ERROR:{user_input} is invalid input. Try again.")

print(int_squares())

#task13
with open("hello.txt", "w") as file:
    file.write("Hello, world!")
print("Text is successfully written in the new file")

#task14
try:
    with open("hello.txt", "r") as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print("Error: File is not found.")
    








