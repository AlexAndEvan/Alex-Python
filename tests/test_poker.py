import unittest
import sys
import os
sys.path += ['..', '../..']
from AlexPython.mylib.poker import Suit
from AlexPython.mylib.poker import Hand
from AlexPython.mylib.poker import HandName
from AlexPython.mylib.poker import ifHand1Win

class TestStringMethods(unittest.TestCase):
    def test_suit(self):
        clubs = Suit("C")
        self.assertEqual(clubs, Suit.clubs)
    def test_is_royal_flush(self):
        test_data = [[('5H', '5C', '6S', '7S', 'KD'), [False]],
        [('2D', '3D', '4D', '5D', '6D'), [False]],
        [('TH', 'JH', 'QH', 'KH', 'AH'), [True, [10, 11, 12, 13, 14]]]]
        self.run_poker_test('is_royal_flush', test_data)
    def test_is_straight_flush(self):
        test_data = [[('5H', '5C', '6S', '7S', 'KD'), [False]],
        [('5H', '6H', '7S', '8S', '9D'), [False]],
        [('2D', '3D', '4D', '5D', '6D'), [True, [2, 3, 4, 5, 6]]],
        [('5H', '6H', '7H', '8H', '9H'), [True, [5, 6, 7, 8, 9]]],
        [('TH', 'JH', 'QH', 'KH', 'AH'), [True, [10, 11, 12, 13, 14]]]]
        self.run_poker_test('is_straight_flush', test_data)
    def test_is_four_of_a_kind(self):
        test_data = [[('5H', '5C', '6S', '7S', 'KD'), [False]],
        [('5H', '6H', '7S', '8S', '9D'), [False]],
        [('2D', '2H', '2S', '2C', '5S'), [True, [2, 2, 2, 2, 5]]],
        [('3H', '3D', '3S', '3C', '9H'), [True, [3, 3, 3, 3, 9]]]]
        self.run_poker_test('is_four_of_a_kind', test_data)
    def test_is_full_house(self):
        test_data = [[('5H', '5C', '6S', '6S', 'KD'), [False]],
        [('5H', '6H', '7S', '8S', '9D'), [False]],
        [('2D', '2H', '2S', '5C', '5S'), [True, [2, 2, 2, 5, 5]]],
        [('3H', '9D', '3S', '3C', '9H'), [True, [3, 3, 3, 9, 9]]]]
        self.run_poker_test('is_full_house', test_data)        
    def test_is_flush(self):
        test_data = [[('5H', '5C', '6S', '6S', 'KD'), [False]],
        [('5H', '6H', '7S', '8S', '9D'), [False]],
        [('2D', '5D', '8D', 'AD', '4D'), [True, [2, 4, 5, 8, 14]]],
        [('8H', 'QH', 'AH', '3H', '9H'), [True, [3, 8, 9, 12, 14]]]]
        self.run_poker_test('is_flush', test_data) 
    def test_is_straight(self):
        test_data = [[('5H', '7C', '6S', '8S', 'KD'), [False]],
        [('5H', '6H', 'AS', '8S', '9D'), [False]],
        [('5H', '6H', '7S', '8S', '9D'), [True, [5, 6, 7, 8, 9]]],
        [('8H', 'TC', '6H', '7H', '9S'), [True, [6, 7, 8, 9, 10]]]]
        self.run_poker_test('is_straight', test_data) 
    def test_is_three_of_a_kind(self):
        test_data = [[('5H', '5C', '6S', '7S', 'KD'), [False]],
        [('5H', '6H', '7S', '8S', '9D'), [False]],
        [('2D', '2H', 'TS', '2C', '5S'), [True, [2, 2, 2, 5, 10]]],
        [('3H', 'AD', '3S', '3C', '9H'), [True, [3, 3, 3, 9, 14]]]]
        self.run_poker_test('is_three_of_a_kind', test_data) 
    def test_is_two_pairs(self):
        test_data = [[('5H', '5C', '6S', '7S', 'KD'), [False]],
        [('5H', '6H', '6S', '8S', '9D'), [False]],
        [('2D', '2H', 'TS', 'TC', '5S'), [True, [2, 2, 5, 10, 10]]],
        [('3H', 'AD', '3S', '9C', '9H'), [True, [3, 3, 9, 9, 14]]]]
        self.run_poker_test('is_two_pairs', test_data) 
    def test_is_one_pair(self):
        test_data = [[('5H', '3C', '6S', '7S', 'KD'), [False]],
        [('5H', '6H', 'TS', '8S', '9D'), [False]],
        [('2D', '2H', 'KS', 'TC', '5S'), [True, [2, 2, 5, 10, 13]]],
        [('3H', 'AD', '3S', '9C', '2H'), [True, [2, 3, 3, 9, 14]]]]
        self.run_poker_test('is_one_pair', test_data) 
    def test_is_high_card(self):
        test_data = [[('5H', '3C', '6S', '7S', 'KD'), [True, [3, 5, 6, 7, 13]]],
        [('5H', '6H', 'TS', '8S', '9D'), [True, [5, 6, 8, 9, 10]]],
        [('2D', '2H', 'KS', 'TC', '5S'), [True, [2, 2, 5, 10, 13]]],
        [('3H', 'AD', '3S', '9C', '2H'), [True, [2, 3, 3, 9, 14]]]]
        self.run_poker_test('is_high_card', test_data) 
    def test_get_hand_name(self):
        test_data = [[('5H', '7C', '6S', '8S', 'KD'), [HandName.high_card, [5, 6, 7, 8, 13]]],
        [('5H', '6H', 'AS', '5S', '9D'), [HandName.one_pair, [5, 5, 6, 9, 14]]],
        [('3H', 'AD', '3S', '9C', '9H'), [HandName.two_pairs, [3, 3, 9, 9, 14]]],
        [('3H', 'AD', '3S', '3C', '9H'), [HandName.three_of_a_kind, [3, 3, 3, 9, 14]]],
        [('5H', '6H', '7S', '8S', '9D'), [HandName.straight, [5, 6, 7, 8, 9]]],
        [('2D', '5D', '8D', 'AD', '4D'), [HandName.flush, [2, 4, 5, 8, 14]]],
        [('2D', '2H', '2S', '5C', '5S'), [HandName.full_house, [2, 2, 2, 5, 5]]],
        [('2D', '2H', '2S', '2C', '5S'), [HandName.four_of_a_kind, [2, 2, 2, 2, 5]]],
        [('5H', '6H', '7H', '8H', '9H'), [HandName.straight_flush, [5, 6, 7, 8, 9]]],
        [('TH', 'JH', 'QH', 'KH', 'AH'), [HandName.royal_flush, [10, 11, 12, 13, 14]]]]
        for data in test_data:
            hand = Hand(data[0])
            result = hand.get_hand_name()
            self.assertEqual(result, data[1], data)
    def run_poker_test(self, test_method, test_data):
        for data in test_data:
            hand = Hand(data[0])
            result = getattr(hand, test_method)()
            self.assertEqual(result[0], data[1][0], data)
            if(result[0]):
                self.assertEqual(result[1], data[1][1], data)
    def test_poker(self):
        # Test with sample data
        test_hands = ('5H', '5C', '6S', '7S', 'KD', '2C', '3S', '8S', '8D', 'TD')
        result = ifHand1Win(test_hands[0:5], test_hands[5:10])
        self.assertFalse(result)

        # Test with data from file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        f = open(dir_path+'/poker.test.data', "r")
        lines = f.readlines()
        for line in lines:
            cards = line.split()
            result = ifHand1Win(cards[0:5], cards[5:10])
            print("ifHand1Win? " + str(result))
        f.close()

if __name__ == '__main__':
    unittest.main()