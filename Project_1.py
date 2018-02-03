# Lab 1.py
# Ethan Sayles
# February 2, 2018
# Purpose: Simulate agents for a card game and run statistics on them.

import random


# Class to define a default player with a name, cards, and a status to tell if still in a round.
class Player:

    def __init__(self, name,cards = [], status=1):
        self.name = name
        self.status = status
        self.cards = cards


    # Called when a player has to pass.
    def skip(self):
        self.cards.append(random.randint(2,15))
        # Ja-11, Q-12, K-13, A-14, Jo-15
        self.status = 0


# Class for the player who implements the  random strategy.
class RandomPlayer(Player):

    def __init__(self, cards=[random.randint(2, 15) for _ in range(10)]):
        Player.__init__(self, "R",cards)
        self.cards = [random.randint(2, 15) for _ in range(10)]

    # Creates a temporary list of valid cards and then uses a random card from that list.
    def play(self, curr_card):
        temp = [x for x in self.cards if x > curr_card]
        if not temp:
            self.skip()
            return curr_card
        else:
            card = temp[random.randint(0, len(temp) - 1)]
            self.cards.remove(card)
            return card


# Class for the player who implements the high strategy
class HighPlayer(Player):

    def __init__(self, cards=[random.randint(2, 15) for _ in range(10)]):
        Player.__init__(self, "H",cards)
        self.cards = [random.randint(2, 15) for _ in range(10)]

    # Plays the highest valid card if possible.
    def play(self, curr_card):
        card = max(self.cards)
        if card <= curr_card:
            self.skip()
            return curr_card
        else:
            self.cards.remove(card)
            return card


# Class for the player who implements the low strategy.
class LowPlayer(Player):

    def __init__(self, cards=[random.randint(2, 15) for _ in range(10)]):
        Player.__init__(self, "L",cards)
        self.cards = [random.randint(2, 15) for _ in range(10)]

    # Creates a temporary list of valid cards and then uses a lowest card from that list.
    def play(self, curr_card):
        temp = [x for x in self.cards if x > curr_card]
        if not temp:
            self.skip()
            return curr_card
        else:
            card = min(temp)
            self.cards.remove(card)
            return card


# Class to keep track of any number of card games.
class CardGame:

    def __init__(self, players=[]):
        self.players = []
        for i in players:
            if i == 'l':
                self.players.append(LowPlayer())
            elif i == 'h':
                self.players.append(HighPlayer())
            elif i == 'r':
                self.players.append(RandomPlayer())
            else:
                print("error")


    # Function that plays a round, and returns the winner of the round.
    def round(self, start):
        new_card = 0
        last_player = -1
        turn = start
        for i in self.players:
            i.status = 1
        while any([i.status for i in self.players]):
            if last_player == turn:
                if not self.players[turn].cards:
                    return [turn, turn]
                # print("New Round")
                return [turn, -1]
            if self.players[turn].status == 1:
                new_card = self.players[turn].play(new_card)
                if self.players[turn].status == 0:
                    pass
                    # print("pass")
                else:
                    last_player = turn
                    #print(new_card)
                    if not self.players[turn].cards:
                        return [turn, turn]
            turn += 1
            if turn == len(self.players):
                turn = 0

    # function to run a full game returning the winner of the game.
    def game(self):
        for i in self.players:
            i.cards  = [random.randint(2,15) for _ in range(10)]
        highest_cards = [max(i.cards) for i in self.players]
        starter = highest_cards.index(max(highest_cards))
        game_condition = self.round(starter)
        while game_condition[1] == -1:
            # print([len(x.cards) for x in self.players])
            game_condition = self.round(game_condition[0])
        return [game_condition[1], starter]

    # function to run an arbitrary number of games and keep track of the winners.
    def stats(self, turns):
        wins = [0 for _ in self.players]
        percent = []
        names = [i.name for i in self.players]
        for _ in range(0, turns):
            win = self.game()
            wins[win[0]] += 1
        for i in wins:
            percent.append((i / turns) * 100)
        print(names)
        return percent


if __name__ == '__main__':
    import sys

    Game = CardGame(sys.argv[2:])
    print(Game.stats(int(sys.argv[1])))
