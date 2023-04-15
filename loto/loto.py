import random

# Еnter your 6 lucky numbers separated by space and comma.
my_numbers = list(map(int, input().split(", ")))
the_numbers = []

counter = 0

while len(the_numbers) < 6:
    winning_numbers = random.randint(1, 49)
    if winning_numbers in the_numbers:
        the_numbers.pop()
    else:
        the_numbers.append(winning_numbers)

print(f"My numbers: {', '.join(list(map(str, my_numbers)))}")
print(f"The winning numbers: {', '.join(list(map(str, the_numbers)))}")

for i in my_numbers:
    if str(i) in str(the_numbers):
        counter += 1

print(f"\nYou have {counter} known numbers in the lottery game: Who wants to be f****d?")
