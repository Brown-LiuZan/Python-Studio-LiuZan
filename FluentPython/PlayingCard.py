#!/usr/local/bin/python3

import collections


Card = collections.namedtuple('Card', ['suit', 'rank'])


class CardPack:
    suits = 'Spades Hearts Clubs Diamonds'.split()
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    x = CardPack()
    print('First card is', x[0])
    print('Last card is', x[-1])
    from random import choice
    [print('Random', i, 'is', choice(x)) for i in range(1, 11)]

