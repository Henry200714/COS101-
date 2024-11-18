
print("This is a program created for Math calculations.")
print("A: Addition")
print("B: Subtraction")
print("C: Multiplication")
print("D: Division")
print("E: Solve Quadratic Equation")
print("Choose an operation between A-E:")
# Ask for user input
inputMsg = input().lower()

# A function to perform addition
def a():
    print("Enter the first number:")
    num1 = float(input())
    print("Enter the second number:")
    num2 = float(input())
    result = num1 + num2
    print(f"The result of addition is {result}.")

# A function to perform subtraction
def b():
    print("Enter the first number:")
    num1 = float(input())
    print("Enter the second number:")
    num2 = float(input())
    result = num1 - num2
    print(f"The result of subtraction is {result}.")

# A function to perform multiplication
def c():
    print("Enter the first number:")
    num1 = float(input())
    print("Enter the second number:")
    num2 = float(input())
    result = num1 * num2
    print(f"The result of multiplication is {result}.")

# A function to perform division
def d():
    print("Enter the numerator:")
    numerator = float(input())
    print("Enter the denominator (non-zero):")
    denominator = float(input())
    while denominator == 0:
        print("Denominator cannot be zero. Please enter a valid value:")
        denominator = float(input())
    result = numerator / denominator
    print(f"The result of division is {result}.")

# A function to solve quadratic equations
def e():
    print("Enter the coefficient a (non-zero):")
    a = float(input())
    while a == 0:
        print("Coefficient 'a' cannot be zero. Enter a valid value:")
        a = float(input())
    print("Enter the coefficient b:")
    b = float(input())
    print("Enter the coefficient c:")
    c = float(input())
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        print(f"The roots are real and different: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"The roots are real and the same: {root}")
    else:
        realPart = -b / (2*a)
        imagPart = (abs(discriminant)**0.5) / (2*a)
        print(f"The roots are complex: {realPart} + {imagPart}i, {realPart} - {imagPart}i")

# Ensures user input provided is case-insensitive
if inputMsg == "a":
    a()
elif inputMsg == "b":
    b()
elif inputMsg == "c":
    c()
elif inputMsg == "d":
    d()
elif inputMsg == "e":
    e()
# Prints an error provided that user input is invalid
else:
    print("Invalid input. Use letters between A-E.")
