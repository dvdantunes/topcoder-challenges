# -*- encoding: utf-8 -*-

"""
SRM 728 - Div 2 (250) - HalvingEasy

@see No editorial found
@see https://community.topcoder.com/stat?c=round_overview&er=5&rd=17064
"""

class HalvingEasy():

    def count(self, S, T):

        def canBeHalvedTo(x, T):
            while x > T:
                x = x // 2

            return x == T

        return len([x for x in S if canBeHalvedTo(x, T)])
