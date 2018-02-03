# cpsc-3520-project-1-spring-2018
# Card Game Simulation

This project simulates agents playing a game that is a mixture of war and feudal wars. In
this game players begin with 10 random cards from a standard deck of cards, including
Jokers. There is an infinitely large draw pile, and the goal state is to have no cards
remaining. On each turn a player may pass, or play a card of higher value than the
current card in play. When passing a player must draw a card and then remain out of
play for the rest of the hand. Once play proceeds with all players passing the owner of
the winning card leads the start of the preceding round, and all players are back in play.

## Getting Started

To get this program running there are no installation steps required. It works out of the box if all the Prerequisites are met. The program will return a list of players as well as the win rate for each player.

### Prerequisites

In order to run this program you will need to have python 3 installed and then random library installed.

```
sudo apt install python3
```

### Installing

In order to run this program you must call it with python3 and provide the arguments of a number of turns to run, followed by a list of players to play where players can be 'l', 'h', or 'r'.

e.g.
```
python3 Lab1.py 1000 l h r l
```
will run 1000 games with two low players, a high player, and a random player.

