import random
import time

print("За край на програмата напиши 'Край'. Много креативно :D\n")

friends = []

while True:
    name = input("Въведи име: ").lower()

    if not name == "край":
        friends.append(name.capitalize())
        continue
    break

how_to_pay_bill = random.choice(friends)

print("\nЖребият е хвърлен!")
time.sleep(3)
print("Името на печелившият е...")
time.sleep(3)
print("Неговото име е...")
time.sleep(3)
print("Той/Тя се казва...")
time.sleep(3)
print("Всички го/я знаят като...")
time.sleep(3)
print("По акт за раждане е записан/а с името...")
time.sleep(3)

print(f"\n{how_to_pay_bill}, вади парите !!!")
