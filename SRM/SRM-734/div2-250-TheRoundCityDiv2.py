# -*- encoding: utf-8 -*-

"""
SRM 734 - Div 2 (250) - TheRoundCityDiv2

@see https://www.topcoder.com/blog/single-round-match-734-editorials/
@see https://community.topcoder.com/stat?c=problem_statement&pm=14898&rd=17158
"""

import math


class TheRoundCityDiv2():

    def find(self, r):

        houses = 0
        for x in range(-r, r+1):
            for y in range(-r, r+1):
                if x == 0 and y == 0:
                    continue

                if math.sqrt(x*x + y*y) <= r:
                    houses += 1

        return houses

