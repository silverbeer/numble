import math

def how_far_away(secret_number, number_guessed):
    if number_guessed > secret_number:
        distance = number_guessed - secret_number
    else:
        distance = secret_number - number_guessed

    print(distance)
    return distance


def round_to_nearest_10(distance):
    return 10 * ((distance + 5) // 10)



min = 1
max = 100
secret_number = 90
number_guessed = 23

distance = how_far_away(secret_number, number_guessed)

hint = round_to_nearest_10(distance)
print(f"Hint:  Your guess was off by around {hint}")




