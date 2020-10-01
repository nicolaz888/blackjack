import constants
import random


class Card():

    def __init__(self, value, pinta):
        self.value = value
        self.pinta = pinta
        self.peso = self.get_peso(self.value)

    def get_peso(self, value):

        if value == 'A':
            return 11
        elif value in constants.letras:
            return 10
        else:
            return int(value)

    def __str__(self):
        return str(self.value)


# card = Card('A')
# print(card)
