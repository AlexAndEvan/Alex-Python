from enum import Enum
class Suit(Enum):
    clubs = "C"
    diamonds = "D"
    hearts = "H"
    spades = "S"

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

