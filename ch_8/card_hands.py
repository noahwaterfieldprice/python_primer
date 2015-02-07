# Exercise 8.7
from Deck import Deck
from cards import same_rank, same_suit


def prob_two_pairs(N=100000):
    M = 0  # no. of successes
    for exp in xrange(N):
        deck = Deck()
        hand = deck.hand(n=5)
        M += (same_rank(hand, 2) == 2)
    return float(M) / N


def prob_same_suit(N=100000):
    M = 0  # no. of successes
    for exp in xrange(N):
        deck = Deck()
        hand = deck.hand(n=5)
        for suit in same_suit(hand):
            M += (same_suit(hand)[suit] in [4, 5])
    return float(M) / N


def prob_fourofakind(N=100000):
    M = 0  # no. of successes
    for exp in xrange(N):
        deck = Deck()
        hand = deck.hand(n=5)
        M += (same_rank(hand, 4) == 1)
    return float(M) / N

print 'Probability of two pairs in five card hand:', \
    prob_two_pairs()
print 'Probability of four or five cards in same suit in five card hand:', \
    prob_same_suit()
print 'Probability of four of a kind in five card hand:', \
    prob_fourofakind()

"""
Sample run:
python card_hands.py
Probability of two pairs in five card hand: 0.04801
Probability of four or five cards in same suit in five card hand: 0.04492
Probability of four of a kind in five card hand: 0.00021
"""
