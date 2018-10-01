# -*- encoding: utf-8 -*-

"""
SRM 734 - Div 2 (250) - TheRoundCityDiv2 [Andras Viewpoint]

@see https://www.topcoder.com/blog/single-round-match-734-editorials/
@see https://community.topcoder.com/stat?c=problem_statement&pm=14898&rd=17158
"""

class TheRoundCityDiv2():

    def find(self, r):

        houses = 0
        for x in range(1, r+1):
            for y in range(0, r+1):     # x's range begins at 1 on purpose to skip (0, 0)

                # This is not needed, r > 0
                # if x == 0 and y == 0:
                #     continue

                if (x*x + y*y) <= r*r:
                    houses += 1

        return houses

