text = input("Convert your message to ASCII code here: ")
print("Use ascii table to decryption.\n")

for i in text:
    current_text = ord(i)
    print(current_text, "-> ", end=" ")

    symbols_of_the_message = chr(current_text)
    print(symbols_of_the_message)
