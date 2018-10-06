# -*- encoding: utf-8 -*-

"""
SRM 730 - Div 2 (250) - IntervalIntersections

@see No editorial found
@see https://community.topcoder.com/stat?c=problem_statement&pm=14814&rd=17087
"""

class IntervalIntersections():

    def minLength(self, x1, y1, x2, y2):

        if y1 <= x2:
            # first interval is the lowest one
            return abs(x2 - y1)

        else:
            # try in reverse order
            # [x2, y2] vs [x1, y1]

            # 0 if they intersect
            return (0 if x1 <= y2 else abs(x1 - y2))

