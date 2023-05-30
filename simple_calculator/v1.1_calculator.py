def calculator(first_number, operator, second_number):
    map_operator = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if not b == 0 else "Error: Division by zero",
        "//": lambda a, b: a // b if not b == 0 else "Error: Division by zero",
        "%": lambda a, b: a % b if not b == 0 else "Error: Division by zero",
        "**": lambda a, b: a ** b,

    }

    if operator in map_operator:
        return f"{first_number} {operator} {second_number} = {map_operator[operator](first_number, second_number)}"
    else:
        return "Error invalid operator."


first_number = float(input("Enter the first number: "))
operator = input("Operator choices from the following options (+, -, *, /, //, **, %): ")
second_number = float(input("Enter the second number: "))

print(calculator(first_number, operator, second_number))
