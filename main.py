import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list

print(hangman_art.logo)
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = word_list[random.randint(0, 2)]

guessed = []

hangman_counter = 0

for i in chosen_word:
    guessed.append("_")

for k in guessed:
    print(k, end=" ")
print("\n")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
while "_" in guessed or hangman_counter < 7:
    while True and "_" in guessed:
        user_letter = input("Make a guess?: ")
        if len(user_letter) == 1 and user_letter not in guessed:
            break
        else:
            print("Not a letter, or already used letter. Please make sure you only type a letter or a new one!")
            True
    if user_letter in chosen_word and "_" in guessed:
        for i in range(0, len(chosen_word)):
            if "_" not in guessed:
                print("you won!")
                break
            elif user_letter == chosen_word[i]:
                guessed[i] = user_letter

    elif user_letter in chosen_word and "_" not in guessed:
        print("You Won!")
        break
    else:
        if hangman_counter < 5:
            hangman_counter += 1
            print(hangman_art.hangmanpics[hangman_counter])
        else:
            print(hangman_art.hangmanpics[6])
            print("Game Over!")
            break

    for i in guessed:
        print(i, end=" ")
    print("\n")
