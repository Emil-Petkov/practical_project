import string
import random
from ascii_art import asart
import time

password = []


def password_generator(n_letters: int, n_numbers: int, n_symbols: int):
    l = string.ascii_letters
    n = string.digits
    s = ["!", "@", "#", "$", "%", "&", "*"]

    for letter in range(0, n_letters):
        password.append(random.choice(l))

    for num in range(0, n_numbers):
        password.append(random.choice(n))

    for sym in range(0, n_symbols):
        password.append(random.choice(s))

    random.shuffle(password)

    print(43 * "_")
    return f"This is your random password: {''.join(password)}"


print(asart)
n_letters = int(input("How many letters you want in your password? "))
n_numbers = int(input("How many numbers you want in your password? "))
n_symbols = int(input("How many symbols you want in your password? "))

result = password_generator(n_letters, n_numbers, n_symbols)
print(result)
time.sleep(92)

