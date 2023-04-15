import random
import time

from art import logo, player_art, shot, goal, missed
from teams import cska, levski

print(logo)

my_team_score = 0
pc_tem_score = 0

pc_goalkeeper = random.randint(1, 7)
player = random.randint(1, 7)

game_over = False
print("""Choice your team at: CSKA or Levski
""")

team_user = "cska"  # input("Choice Your team: ").lower()  # input

if team_user == "cska":
    print("""Choice your goalkeeper:\n1.Gustavo Busatto\n2.Dimitar Evtimov""")
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
    time.sleep(2)
    print("and...\n")
    time.sleep(2)

    if player == pc_goalkeeper:
        print(missed)
    else:
        print(goal)
        my_team_score += 1

    if player == 1:
        print(f"{current_player} choice left")
    elif player == 2:
        print(f"{current_player} choice right")
    elif player == 3:
        print(f"{current_player} choice center")
    elif player == 4:
        print(f"{current_player} choice up left corner")
    elif player == 5:
        print(f"{current_player} choice up right corner")
    elif player == 6:
        print(f"{current_player} choice down left corner")
    elif player == 7:
        print(f"{current_player} choice down right corner")

    if pc_goalkeeper == 1:
        print("Goalkeeper choice left")
    elif pc_goalkeeper == 2:
        print("Goalkeeper choice right")
    elif pc_goalkeeper == 3:
        print("Goalkeeper choice center")
    elif pc_goalkeeper == 4:
        print("Goalkeeper choice up left corner")
    elif pc_goalkeeper == 5:
        print("Goalkeeper choice up right corner")
    elif pc_goalkeeper == 6:
        print("Goalkeeper choice down left corner")
    elif pc_goalkeeper == 7:
        print("Goalkeeper choice down right corner")







elif team_user.lower() == "levski":
    pass

    print("Error. Wrong team!")
else:
    exit()

print()
print(f"Home {my_team_score} : {pc_tem_score} Away")
