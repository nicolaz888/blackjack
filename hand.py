import constants
import random
import card


class Hand():

    def __init__(self, *cards):
        self.cards = [*cards]

    def add_card(self, card_random):
        self.cards.append(card_random)

    def get_peso(self):
        resp = 0
        for item in self.cards:
            resp += item.peso

        if resp > 21:
            for item in self.cards:
                if item.value == 'A' and resp > 21:
                    resp -= item.peso
                    resp += 1

        return resp

    def __str__(self):
        resp = ''

        for item in self.cards:
            resp += str(item.value) + ', '

        return resp[:-2]
