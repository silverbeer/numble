import random

#  Welcome to the game
print("Welcome to the Numble Game")

#  What is your name?
player_name = input("What is your name? ")
print(f"Hi!  Welcome to Numble.")

#  Min Number
min = int(input("Min Number: "))
#print(min)

#  Max Number
max = int(input("Max Number: "))
#print(max)

#  Max number of guesses
number_of_guesses = int(input("Number of guesses: "))
#print(number_of_guesses)

#   Randomly select number
secret_number = random.randint(min, max)
#print(f"secret number = {secret_number}")

guess_count = 0
list_of_numbers = []
#  Play the game
while True:

    number_guessed = int(input("Guess a number: "))
    guess_count += 1
    list_of_numbers.append(number_guessed)

    if number_guessed == secret_number:
        print("OMG you won the game!!!!!!!")
        break

    if number_guessed < secret_number:
        print("HIGHER")
    else:
        print("LOWER")

    if guess_count < number_of_guesses:
        #print(f"guess count = {guess_count}")
        #print(f"the list of guesses: {list_of_numbers}")

        continue
    else:
        print(f"Sorry you ran out of guesses and lost the game. The correct number was {secret_number}")
        break