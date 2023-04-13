print("Welcome to the tip calculator!")
print()
bill = float(input("What was the total bill? $: "))
tip = int(input("How much tip would you like to give? 0, 5, 10, 12, 15: "))
people = int(input("How many people to split the bill?: "))

tip_as_percent = (bill * tip) / 100
total_per_person = (bill + tip_as_percent) / people

print()
print(f"${total_per_person:.2f}")
