def addition(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

def subtraction(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"

def multiplication(num1, num2):
    return f"{num1} X {num2} = {num1 * num2}"

def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return f"{num1} ÷ {num2} = {num1 / num2}"

menu = """
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
"""

print("Welcome to the Simple Calculator")
while True:
    print(menu)
    choice = int(input("Choose an option from the menu: "))
    if choice == 5:
        print("Goodbye!")
        break

    if choice not in [1, 2, 3, 4]:
        print("Enter a valid choice from the menu")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        print(addition(num1, num2))
    elif choice == 2:
        print(subtraction(num1, num2))
    elif choice == 3:
        print(multiplication(num1, num2))
    elif choice == 4:
        print(division(num1, num2))