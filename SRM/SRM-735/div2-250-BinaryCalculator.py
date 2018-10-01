# -*- encoding: utf-8 -*-

"""
SRM 735 - Div 2 (250) - BinaryCalculator

@see https://www.topcoder.com/blog/single-round-match-735-editorials/
@see https://community.topcoder.com/stat?c=round_overview&rd=17158
"""

class BinaryCalculator():

    def minimumSteps(self, a, b):
        numSteps = 0
        while (a != b):
            if a < b:
                a += 3
            else:
                a -= 2

            numSteps += 1

        return numSteps
