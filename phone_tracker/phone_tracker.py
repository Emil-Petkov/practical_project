def phone_tracker(number):
    import phonenumbers
    from phonenumbers import timezone, geocoder, carrier

    phone = phonenumbers.parse(number)

    time = timezone.time_zones_for_number(phone)

    carrier = carrier.name_for_number(phone, 'en')

    country = geocoder.description_for_number(phone, "en")

    print(phone)
    print(time)
    print(carrier)
    print(country)


while True:

    phone_tracker(input("Enter phone number with + and country code: "))
    command = input("Do you want to continue? (y/n): ").lower()

    if command == 'y':
        continue
    elif command == 'n':
        print("Have a good day!")
        break
    else:
        print("Invalid command")
        break
