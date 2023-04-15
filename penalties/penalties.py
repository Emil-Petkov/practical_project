import random
import time

from art import logo, player_art, shot, goal, missed
from teams import cska, levski

print(logo)

my_team_score = 0
pc_team_score = 0

pc_goalkeeper = random.randint(1, 7)
user_goalkeeper = random.randint(1, 7)
pc_goalkeeper_name_cska = random.choice(cska[0]["goalkeeper_name"])
pc_goalkeeper_name_levski = random.choice(levski[0]["goalkeeper_name"])
user_player = random.randint(1, 7)
pc_player = random.randint(1, 7)

game_over = False
print("Choice your team at: CSKA or Levski\n")

team_user = "cska"  # input("Choice Your team: ").lower()  # input

if team_user == "cska":
    print("Choice your goalkeeper:\n1.Gustavo Busatto\n2.Dimitar Evtimov")
    choice_goalkeeper = 1  # int(input(">>> "))
    if choice_goalkeeper == 1:
        keeper = cska[0]["goalkeeper_name"][0]
    elif choice_goalkeeper == 2:
        keeper = cska[0]["goalkeeper_name"][1]
    else:
        print("Wrong choice.")
        exit()
    print()
    print(f"Your goalkeeper is {keeper}.")
    print("Let's play!\n")

    current_player = cska[1]["player_name"][0]
    print(f"{current_player} is shooting...")
    print(shot)
    time.sleep(0)
    print("and...\n")
    time.sleep(0)

    if user_player == pc_goalkeeper:
        print(missed)
    else:
        print(goal)
        my_team_score += 1

    if user_player == 1:
        print(f"{current_player} choice left")
    elif user_player == 2:
        print(f"{current_player} choice right")
    elif user_player == 3:
        print(f"{current_player} choice center")
    elif user_player == 4:
        print(f"{current_player} choice up left corner")
    elif user_player == 5:
        print(f"{current_player} choice up right corner")
    elif user_player == 6:
        print(f"{current_player} choice down left corner")
    elif user_player == 7:
        print(f"{current_player} choice down right corner")

    if pc_goalkeeper == 1:
        print(f"{pc_goalkeeper_name_levski} choice left")
    elif pc_goalkeeper == 2:
        print(f"{pc_goalkeeper_name_levski} choice right")
    elif pc_goalkeeper == 3:
        print(f"{pc_goalkeeper_name_levski} choice center")
    elif pc_goalkeeper == 4:
        print(f"{pc_goalkeeper_name_levski} choice up left corner")
    elif pc_goalkeeper == 5:
        print(f"{pc_goalkeeper_name_levski} choice up right corner")
    elif pc_goalkeeper == 6:
        print(f"{pc_goalkeeper_name_levski} choice down left corner")
    elif pc_goalkeeper == 7:
        print(f"{pc_goalkeeper_name_levski} choice down right corner")

    if user_goalkeeper == 1:
        user_keeper_direction ="choice left"
    elif user_goalkeeper == 2:
        user_keeper_direction = "choice right"
    elif user_goalkeeper == 3:
        user_keeper_direction = "choice center"
    elif user_goalkeeper == 4:
        user_keeper_direction = "choice up left corner"
    elif user_goalkeeper == 5:
        user_keeper_direction = "choice up right corner"
    elif user_goalkeeper == 6:
        user_keeper_direction = "choice down left corner"
    elif user_goalkeeper == 7:
        user_keeper_direction = "choice down right corner"

    if pc_player == 1:
        current_pc_player = "choice left"
    elif pc_player == 2:
        current_pc_player = "choice right"
    elif pc_player == 3:
        current_pc_player = "choice center"
    elif pc_player == 4:
        current_pc_player = "choice up left corner"
    elif pc_player == 5:
        current_pc_player = "choice up right corner"
    elif pc_player == 6:
        current_pc_player = "choice down left corner"
    elif pc_player == 7:
        current_pc_player = "choice down right corner"

    if pc_goalkeeper == 1:
        print(f"{keeper} choice left")
    elif pc_goalkeeper == 2:
        print(f"{keeper} choice right")
    elif pc_goalkeeper == 3:
        print(f"{keeper} choice center")
    elif pc_goalkeeper == 4:
        print(f"{keeper} choice up left corner")
    elif pc_goalkeeper == 5:
        print(f"{keeper} choice up right corner")
    elif pc_goalkeeper == 6:
        print(f"{keeper} choice down left corner")
    elif pc_goalkeeper == 7:
        print(f"{keeper} choice down right corner")

print(f"Home {my_team_score} : {pc_team_score} Away\n")
print("_" * 50)
######## levski turn ###############

print("Levski turn")

first_pc_player = levski[1]['player_name'][0]
print(f"{first_pc_player} is shooting")
print(shot)
print("and...")
time.sleep(2)

if pc_goalkeeper == user_player:
    print(missed)
else:
    print(goal)
    pc_team_score += 1

print(f"{keeper} {user_keeper_direction}")
print(f"{first_pc_player} {current_pc_player}")

print(f"Home {my_team_score} : {pc_team_score} Away\n")
print("_" * 50)

######## cska turn ###############
print("CSKA turn\n")
current_player = cska[1]["player_name"][1]
print(f"{current_player} is shooting...")
print(shot)
time.sleep(0)
print("and...\n")
time.sleep(0)

if pc_goalkeeper == user_player:
    print(missed)
else:
    print(goal)
    my_team_score += 1


print(f"Home {my_team_score} : {pc_team_score} Away\n")
print("_" * 50)
