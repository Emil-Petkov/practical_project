import random
import string

print("Welcome to my Password Generator : )\n")

n_n = int(input("How many numbers would you like in your password? "))
n_l = int(input("How many letters would you like in your password? "))
n_c = int(input("How many symbols would you like in your password? "))

numbers = string.digits
letters = string.ascii_letters
symbols = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "<", ">", "{", "}", "[", "]", "|"]

password = []

for n in range(1, n_n + 1):
    password.append(random.choice(numbers))
for l in range(1, n_l + 1):
    password.append(random.choice(letters))
for c in range(1, n_c + 1):
    password.append(random.choice(symbols))

print()
random.shuffle(password)
print(f'This is your password: -> {"".join(password)}')
