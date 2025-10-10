#task 1
age = 25
name = "Maria"

print(age)
print(name)

# Task 2: Type Conversion
length = 10.5
int_length = int(length)
print(type(length))
print(type(int_length))

# Task 3: Formatted Printing
x = 5
y = 10.5
z = "Hello"
print(f"x: {x}, y: {y}, z: {z}")

# Task 4: Simple Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Maria"))

# Task 5: Conditional Statements
def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))


# Task 12: User Input and Error Handling
while True:
    user_input = input("Enter an integer: ")
    try:
        num = int(user_input)
        print(f"Square: {num ** 2}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Task 13: File Writing
try:
    with open("hello.txt", "w") as f:
        f.write("Hello, World!")
    print("Successfully wrote to hello.txt.")
except Exception as e:
    print(f"Error writing to file: {e}")

# Task 14: File Reading
try:
    with open("hello.txt", "r") as f:
        content = f.read()
    print("Contents of hello.txt:")
    print(content)
except FileNotFoundError:
    print("hello.txt does not exist.")

# Task 15: File Processing
try:
    with open("numbers.txt", "r") as f:
        lines = f.readlines()
    numbers = []
    for line in lines:
        try:
            numbers.append(float(line.strip()))
        except ValueError:
            print(f"Non-numeric data found and skipped: {line.strip()}")
    if numbers:
        total = sum(numbers)
        average = total / len(numbers)
        print(f"Sum: {total}")
        print(f"Average: {average}")
    else:
        print("No valid numbers found in numbers.txt.")
except FileNotFoundError:
    print("numbers.txt does not exist.")