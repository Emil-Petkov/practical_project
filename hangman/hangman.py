import random
from lst_of_words import word_list
from ascii_art_hangman_and_logo import stages, logo
from replit import clear

print(logo)
is_end_fo_the_game = False
lives = len(stages) - 1
print()

random_word = random.choice(word_list).lower()
word_length = len(random_word)
display = []

for _ in range(word_length):
    display.append("_")

while not is_end_fo_the_game:
    print(' '.join(display))
    print()
    guess_letter = input("Guess a letter: ").lower()
    print()
    clear()

    for position in range(word_length):
        letter = random_word[position]
        if letter == guess_letter:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess_letter not in random_word:
        print()
        print(f"You guessed ({guess_letter}), that's not in the word.")
        print()
        lives -= 1

        if lives == 0:
            is_end_fo_the_game = True
            print(f"You lose :(\nThe word was: {random_word}\nTry again.")

    if "_" not in display:
        is_end_fo_the_game = True
        print()
        print(f"The word is {random_word}. You Win : )")

    print(stages[lives])
