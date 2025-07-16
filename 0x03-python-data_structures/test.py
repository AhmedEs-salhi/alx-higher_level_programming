#!/usr/bin/python3
import random
film_list = [
    "Luck",
    "Source Code",
    "The great hack",
    "The pianist",
    "A hero",
    "Casper",
    "The tuxedo",
    "The Theory of Everything"
]

chosen_film = film_list[random.randrange(0, len(film_list))]
print(chosen_film)
