# Number randomly generated 
# Give user a clue to guess
# need to use conditions to guide clues e.g if random no.%2...
# if user guesses wrong another clue, score reduces

import random
print("Hey, welcome\nThis game allows you guess between the numbers 0 - 20\nTry guess right on your first try!\n...GOOD LUCK!\n")

no = random.randint(0, 20)
print(no)

user_guess = int(input("Guess the number: "))
if user_guess == no:
        print("Correct you guessed right!")

while user_guess != no:
    if user_guess == no:
        print("Correct you guessed right!")
    elif user_guess < no:
            print("Wrong, Number is to low")
    elif user_guess > no:
            print("Wrong, Number is to high")         
    user_guess = int(input("Guess the number: "))
    if user_guess == no:
        print("Correct you guessed right!")
        