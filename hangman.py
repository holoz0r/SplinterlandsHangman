# Splinerlands Hangman by holoz0r - from day 7 of "100 days of code" in Python 

import random
from hangmanart import *
from hangmanwords import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word and lives >0:
      lives -= 1
      print(f"You have {lives} lives left.")
      if lives == 0:
        end_of_game = True
        print("You Lose!")
        print(f"The Correct answer was {chosen_word}.")
    print(f"{' '.join(display)}")

    if "_" not in display:
      end_of_game = True
      print("You win.")

    print(stages[lives])
