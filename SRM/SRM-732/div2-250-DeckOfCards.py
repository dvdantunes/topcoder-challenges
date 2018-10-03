# -*- encoding: utf-8 -*-

"""
SRM 732 - Div 2 (250) - DeckOfCards

@see No editorial found
@see https://community.topcoder.com/stat?c=round_overview&er=5&rd=17103
"""

class DeckOfCards():

    def IsValid(self, n, value, suit):

        suitList = list(suit)

        cards = []
        for i in range(n):
            cards.append([value[i], suitList[i]])


        def repeated(cards, c):
            return cards.count(c) > 1

        if len([x for x in cards if repeated(cards, x)]) > 0:
            return "Not perfect"


        for i in range(n):
            card1Value = cards[i][0]
            card1Suit = cards[i][1]

            for j in range(n):
                if i == j:
                    continue

                card2Value = cards[j][0]
                card2Suit = cards[j][1]
                if not ([card1Value, card2Suit] in cards) and not ([card2Value, card1Suit] in cards):
                    return "Not perfect"

        return "Perfect"
