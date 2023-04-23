import time

print("Attention! You have 5 attempts before locking your account.\n")

counter_wrong_try = 0

while True:
    if counter_wrong_try > 4:
        print("\nYour account is locked.\nHave a nice day :)")
        time.sleep(10)
        exit()
    else:
        correct_password = 1703

        user_input = int(input("Enter your password: "))

        if user_input == correct_password:
            print("\nWelcome in your account!")
            time.sleep(10)
            break
        else:

            while True:
                q = 4 - counter_wrong_try
                print(f"Wrong password you have {q} attempts before the account is locked.\n")
                counter_wrong_try += 1
                break
            continue
