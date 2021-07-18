import random
import string

print('H A N G M A N\n')

def game():
    list_of_words = ['python', 'java', 'kotlin', 'javascript']
    secret_word = random.choice(list_of_words)

    attempts = 8

    word = '-' * (len(secret_word))
    guessed_letters = []

    while attempts > 0:
        print()
        print(word)
        letter = input("Input a letter: ")

        if letter in guessed_letters:
            print("You've already guessed this letter")
            continue
        elif len(letter) != 1:
            print("You should input a single letter")
            continue
        elif letter not in list(string.ascii_lowercase):
            print("Please enter a lowercase English letter")
            continue
        elif letter not in secret_word:
            attempts -= 1
            print("That letter doesn't appear in the word")

        for i in range(secret_word.count(letter)):
            letter_position = secret_word.index(letter)
            word = word[:letter_position] + letter + word[letter_position+1:]

        guessed_letters.append(letter)

        if '-' not in word:
            print("You survived!")
            break

    if '-' in word:
        print("You lost!")

    print("""Thanks for playing!
    We'll see how well you did in the next stage""")

    return


while True:
    start_game = input('Type "play" to play the game, "exit" to quit:')
    if start_game == 'play':
        game()
    elif start_game == 'exit':
        break
    else:
        continue
