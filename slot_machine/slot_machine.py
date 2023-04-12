import random
import time
from art import machine

counter = 0
money_cost = 0
price_per_one_try = 1.25
jackpot = 100
print(f"{machine}\n")
print(
    f"Price per one try is ${price_per_one_try}\n\nThe Jackpot is: ${jackpot:.2f}\n\nYou must be 18 years old to play!")
age = int(input("How old are you?: "))

if age < 18:
    print("\nYou are very young!\nBye my little friend!")
    time.sleep(5)
    exit()
elif age > 90:
    print()
    print(f"Don't do nonsense.\nYou are {age} years old.\nDidn't you realize this is\nrigged and I'm robbing you.")
    time.sleep(10)
    exit()
else:
    print("Let's game!\n")

while True:
    def slot_machine(first_number, second_number, third_number, fourth_number, fifth_number):
        if all(num == first_number for num in [second_number, third_number, fourth_number, fifth_number]):
            print(f"Current spin is: {counter}\n")

            print(f"|{first_number}| |{second_number}| |{third_number}| |{fourth_number}| |{fifth_number}|")
            print("Jackpot\n")
            print("_" * 40)
            print(f"You won the Jackpot on the {counter}th attempt")
            print("_" * 40)
            print(f"You gave ${money_cost:.2f} until you hit the jackpot.")
            print(f"You won ${jackpot - money_cost:.2f} after expenses.")
            time.sleep(10)
            exit()
        else:
            print(f"Current spin is: {counter}\n")

            print(f"|{first_number}| |{second_number}| |{third_number}| |{fourth_number}| |{fifth_number}|")
            print("Try again")
            print("_" * 40)
            if jackpot <= money_cost:
                print(
                    f"For {counter} spins you lose ${counter * price_per_one_try:.2f} at a jackpot of ${jackpot:.2f}")
                time.sleep(10)
                exit()


    money_cost += price_per_one_try
    counter += 1

    first_number = random.randint(0, 9)
    second_number = random.randint(0, 9)
    third_number = random.randint(0, 9)
    forth_number = random.randint(0, 9)
    fifth_number = random.randint(0, 9)

    slot_machine(first_number, second_number, third_number, forth_number, fifth_number)
