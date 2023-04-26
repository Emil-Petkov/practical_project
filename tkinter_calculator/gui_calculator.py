import tkinter as tk
from tkinter import messagebox


def add(f_num, s_num):
    return f_num + s_num


def subtract(f_num, s_num):
    return f_num - s_num


def multiply(f_num, s_num):
    return f_num * s_num


def divide(f_num, s_num):
    return f_num / s_num


def calculate():
    first_number = num1.get()
    second_number = num2.get()

    if not first_number.isdigit():
        messagebox.showerror("Error", "First number is not a digit")
        return

    if not second_number.isdigit():
        messagebox.showerror("Error", "Second number is not a digit")
        return

    operator = operator_var.get()

    if operator == "+":
        result = add(float(first_number), float(second_number))

    elif operator == "-":
        result = subtract(float(first_number), float(second_number))

    elif operator == "*":
        result = multiply(float(first_number), float(second_number))

    elif operator == "/":
        result = divide(float(first_number), float(second_number))

    else:
        messagebox.showerror("Error", "Invalid operator")
        return

    result_var.set(result)


root = tk.Tk()
root.title("Calculator")

num1_label = tk.Label(root, text="First Number:")
num1_label.grid(row=0, column=0)

num1 = tk.Entry(root)
num1.grid(row=0, column=1)

num2_label = tk.Label(root, text="Second Number:")
num2_label.grid(row=1, column=0)

num2 = tk.Entry(root)
num2.grid(row=1, column=1)

# Create the operator dropdown
operator_var = tk.StringVar()
operator_var.set("+")

operator_label = tk.Label(root, text="Operator:")

operator_label.grid(row=2, column=0)

operator_dropdown = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_dropdown.grid(row=2, column=1)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

# Create the result label
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0)

result_var = tk.StringVar()
result_var.set("")

result = tk.Label(root, textvariable=result_var)
result.grid(row=4, column=1)

# Start the main loop
root.mainloop()
