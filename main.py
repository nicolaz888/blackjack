import random
import hand
import card
import constants


class Game():

    def __init__(self):
        self.deck = []

    def start(self):

        money = 1000

        while money > 0:

            self.deck = []

            for pinta in constants.pintas:
                for value in constants.values:
                    carta = card.Card(value, pinta)
                    self.deck.append(carta)

            mano_dealer = self.create_hand()
            mano_player = self.create_hand()
            print(f'\nthis is your hand: {mano_player}')

            while True:

                move = input('\nEnter h to hit or s to stand: ')

                if move == 'h':
                    mano_player.add_card(self.get_card())
                    peso_mano = mano_player.get_peso()
                    if peso_mano > 21:
                        # print('U passed away :S')
                        pass

                elif move == 's':
                    peso_dealer = mano_dealer.get_peso()
                    while peso_dealer < 21:
                        if peso_dealer in [18, 19, 20, 21]:
                            break
                        mano_dealer.add_card(self.get_card())
                        peso_dealer = mano_dealer.get_peso()

                    peso_mano = mano_player.get_peso()

                    print(
                        f'\nthis is your hand now: {mano_player} -> {mano_player.get_peso()}')
                    print(
                        f'\nthis is dealer hand now: {mano_dealer} -> {mano_dealer.get_peso()}')

                    if peso_mano <= 21 >= peso_dealer < peso_mano:
                        print('GANASTE :D !!')
                        money += 100
                    elif peso_mano <= 21 and peso_dealer > 21:
                        print('GANASTE :D !!')
                        money += 100
                    elif peso_mano > 21 < peso_dealer:
                        print('EMPATE :/ !!')
                    else:
                        print('PERDISTE :_( !!')
                        money -= 100

                    print(f'te quedan {money} tokens')

                    break

                elif move == 'r':
                    del self
                    game = Game()
                    game.start()

                print(
                    f'\nthis is your hand now: {mano_player} -> {mano_player.get_peso()}')
                # print(
                #     f'this is dealer hand now: {mano_dealer} -> {mano_dealer.get_peso()}')

            resp = input('\nDesea jugar otra partida? y o n: ')
            if resp == 'y':
                continue
            elif resp == 'n':
                break

    def create_hand(self):
        card1 = self.get_card()
        card2 = self.get_card()
        mano = hand.Hand(card1, card2)
        # print(f'card1: {card1} and card2: {card2}')
        return mano

    def get_card(self):
        return self.deck.pop(random.randint(0, len(self.deck)-1))


if __name__ == '__main__':
    game = Game()
    game.start()
