from enum import Enum
from itertools import groupby
from collections import Counter

class Suit(Enum):
    clubs = 'C'
    diamonds = 'D'
    hearts = 'H'
    spades = 'S'
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class HandName(Enum):
    royal_flush = 1
    straight_flush = 2
    four_of_a_kind = 3
    full_house = 4
    flush = 5
    straight = 6
    three_of_a_kind = 7
    two_pairs = 8
    one_pair = 9
    high_card = 10
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented   

hand_name_order = [x.name for x in list(HandName)]

rank_def = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}  

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        

class Hand:
    def __init__(self, hand_tuple):
        self.cards = []
        for card_string in hand_tuple:
            (rank, suit) = tuple(card_string)
            card = Card(rank_def[rank], Suit(suit))
            self.cards += [card]   
        self.sorted_by_rank = sorted([x.rank for x in self.cards])
        self.cards = sorted(self.cards, key = lambda x: x.suit)
        self.suits = [x.suit for x in self.cards]
    
    def is_straight_internal(self, start):
        return (Counter(self.sorted_by_rank) == Counter(range(start, start+5)))

    def is_royal_flush(self):
        is_straight_from_ten = self.is_straight_internal(10)
        is_same_suit = (Counter(self.suits).most_common(1)[0][1] == 5)
        return [is_straight_from_ten and is_same_suit, self.sorted_by_rank]
    
    def is_straight_flush(self):
        is_straight = self.is_straight_internal(self.sorted_by_rank[0])
        is_same_suit = (Counter(self.suits).most_common(1)[0][1] == 5)
        return [is_straight and is_same_suit, self.sorted_by_rank]

    def is_four_of_a_kind(self):
        return [(Counter(self.sorted_by_rank).most_common(1)[0][1] == 4), self.sorted_by_rank]

    def is_full_house(self):
        counter = Counter(self.sorted_by_rank).most_common(2)
        return [(counter[0][1] == 3 and counter[1][1] == 2), self.sorted_by_rank]

    def is_flush(self):
        return [(Counter(self.suits).most_common(1)[0][1] == 5), self.sorted_by_rank]

    def is_straight(self):
        return [self.is_straight_internal(self.sorted_by_rank[0]), self.sorted_by_rank]

    def is_three_of_a_kind(self):
        return [(Counter(self.sorted_by_rank).most_common(1)[0][1] == 3), self.sorted_by_rank]

    def is_two_pairs(self):
        rank_counter = Counter(self.sorted_by_rank).most_common(2)
        return [(rank_counter[0][1] == 2 and rank_counter[1][1] == 2), self.sorted_by_rank]
    
    def is_one_pair(self):
        rank_counter = Counter(self.sorted_by_rank).most_common(2)
        return [(rank_counter[0][1] == 2 and rank_counter[1][1] == 1), self.sorted_by_rank]
    
    def is_high_card(self):
        return [True, self.sorted_by_rank]
    
    def get_hand_name(self):
        for hand_name in hand_name_order:
            method_name = 'is_' + hand_name
            result = getattr(self, method_name)()
            if(result[0]):
                return [getattr(HandName, hand_name), result[1]]

def ifHand1Win(hand1_input, hand2_input):
    hand1 = Hand(hand1_input)
    hand2 = Hand(hand2_input)
    hand_name_1, ordered_rank_1 = hand1.get_hand_name()
    hand_name_2, ordered_rank_2 = hand2.get_hand_name()
    ordered_rank_1.reverse()
    ordered_rank_2.reverse()

    print("----------------")
    print("---hand 1:" + str(hand1_input) + ":" + hand_name_1.name)
    print("---hand 2:" + str(hand2_input) + ":" + hand_name_2.name)

    if hand_name_1 < hand_name_2:
        return True
    elif hand_name_1 > hand_name_2:
        return False
    # tie breaking logic bellow
    elif hand_name_1 == HandName.royal_flush:
        return False # it's a tie for royal flush
    elif hand_name_1 == HandName.straight_flush or \
         hand_name_1 == HandName.straight:
        return ordered_rank_1[0] > ordered_rank_2[0]
    elif hand_name_1 == HandName.four_of_a_kind or \
         hand_name_1 == HandName.full_house or \
         hand_name_1 == HandName.three_of_a_kind:
        return Counter(ordered_rank_1).most_common(1)[0][0] > Counter(ordered_rank_2).most_common(1)[0][0]
    elif hand_name_1 == HandName.flush or \
         hand_name_1 == HandName.high_card:
        for i in range(len(ordered_rank_1)): 
            if ordered_rank_1[i]!=ordered_rank_2[i]:
                return ordered_rank_1[i] > ordered_rank_2[i]
        return False
    elif hand_name_1 == HandName.two_pairs or \
         hand_name_1 == HandName.one_pair:
        hand_1_counter = [x[0] for x in Counter(ordered_rank_1).most_common()]
        hand_2_counter = [x[0] for x in Counter(ordered_rank_2).most_common()]
        for i in range(len(hand_1_counter)): 
            if hand_1_counter[i]!=hand_2_counter[i]:
                return hand_1_counter[i] > hand_2_counter[i]
        return False


