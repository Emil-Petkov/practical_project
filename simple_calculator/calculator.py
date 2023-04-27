def add(f_num, s_num):
    return f_num + s_num


def subtract(f_num, s_num):
    return f_num - s_num


def multiply(f_num, s_num):
    return f_num * s_num


def divide(f_num, s_num):
    return f_num / s_num


while True:
    user_input = input("To continue press (у) and to end the program press (n): ").lower()

    if user_input == "n":
        print("Have a nice day!")
        break
    elif user_input == "y":

        try:

            first_number = float(input("Enter first number: "))
            operator = input("Operator: ")
            second_number = float(input("Enter second number: "))

            if operator == "+":
                print(f"{first_number} + {second_number} = {add(first_number, second_number)}\n")
            elif operator == "-":
                print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}\n")
            elif operator == "*":
                print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}\n")
            elif operator == "/":
                if second_number == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                else:
                    print(f"{first_number} / {second_number} = {divide(first_number, second_number)}\n")

            else:
                raise ValueError("Invalid operator")

        except ZeroDivisionError as e:
            print(f"{e}. Error: 1723\n")

        except ValueError as e:
            print(e)
            print("Enter only numbers and valid operator (+, -, *, /) please.\n")

        except Exception as e:
            print(e)
            print("Something went wrong.\n")

    else:
        print("Invalid choice.")
        break
