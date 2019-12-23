from Player import Player
from Deck import Deck
import time
from random import randint


class Blackjack:
    def __init__(self,players):
        self.players = players
        self.active_player_index = 0
        self.deck = Deck()
        self.deck.shuffle(3)
        self.card_index = 0
        self.revealed = 0

    def deal(self):
        for _ in range(2):
            for player in self.players:
                player._cards.append(self.deck.cards[self.card_index])
                self.card_index += 1
                player.order_cards()
    
    def next_player(self):
        self.active_player_index += 1
    
    def active_player(self):
        return self.players[self.active_player_index]
    
    # def ask_bet(self):
    #     bet = input("Place your bet: ")
    #     if int(bet) > self.player.funds:
    #         print(f"Insufficient funds. Your balance: {self.player.funds}")
    #         self.ask_bet()
    #     else:
    #         self.player.set_bet(bet)
    

    def hit(self, player):
        new_card = (self.deck.cards[self.card_index])
        player._cards.append(new_card)
        self.card_index += 1
        return new_card
    
    # def reveal_dealer(self):
    #     self.revealed = 1
    
    # def get_winner(self):
    #     if self.get_value(self.player) > self.dealer_value() and self.get_value(self.player) <= 21 or self.dealer_value() > 21:
    #         print("You win!")
    #         self.player.funds += self.player.bet * 2
    #     elif self.get_value(self.player) == self.dealer_value():
    #         self.player.funds += self.player.bet
        
    #     self.player.set_bet(0)

# def print_board(game):
#     print("\n" * 100)
#     game.show_cards(game.dealer)
#     game.show_cards(game.player)
#     print("\n")


    # move = 0

    # while move != 1:
    #     move = int(input("Hit (0) or Stay (1)?: "))
        # if move == 0:
        #     game.hit(game.player)
        #     game.player.order_cards()
        #     print_board(game)
        #     value = game.get_value(player)
        #     if value == 21:
        #         break
        #     elif value > 21:
        #         print("BUST")
        #         break

    # while game.dealer_value() < 18 and game.get_value(player) < 22:
    #     game.hit(game.dealer)
    #     game.dealer.order_cards()
    #     print_board(game)
    #     time.sleep(4)

    # game.get_winner()

    # game.reveal_dealer()

    # print_board(game)

    # playing = int(input("Play again?: "))