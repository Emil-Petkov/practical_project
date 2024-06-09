def display_parties(parties):
    print("Изберете партия или коалиция:")
    for key, value in parties.items():
        print(f"{key}: {value['name']}")


def display_preferences(preferences):
    if preferences:
        print("\nИзберете преференция:")
        for key in preferences:
            print(f"{key}")


political_party_or_coalition = {
    1: {'name': 'Партия 1', 'преференции': [101, 102, 103]},
    2: {'name': 'Партия 2', 'преференции': [201, 202, 203]},
    3: {'name': 'Партия 3', 'преференции': [301, 302, 303]},
    4: {'name': 'Не подкрепям нищожества!', 'преференции': []}
}


def vote():
    display_parties(political_party_or_coalition)
    party_choice = int(input("\nВъведете номера на избраната партия: "))

    if party_choice in political_party_or_coalition:
        selected_party = political_party_or_coalition[party_choice]
        preference_choice = None

        if selected_party['преференции']:
            display_preferences(selected_party['преференции'])
            preference_choice = int(input("Въведете преференция (или 0 за без преференция): "))
            if preference_choice not in selected_party['преференции'] and preference_choice != 0:
                print("Невалидна преференция!")
                return

        print(f"\nВие гласувахте за: {selected_party['name']}")
        if preference_choice and preference_choice != 0:
            print(f"с преференция: {preference_choice}")
    else:
        print("Невалидна партия!")


print('Разяснение за дебили вярващи на пропаганда!\n')
vote()
