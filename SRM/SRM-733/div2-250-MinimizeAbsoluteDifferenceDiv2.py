# -*- encoding: utf-8 -*-

"""
SRM 733 - Div 2 (250) - MinimizeAbsoluteDifferenceDiv2

@see https://www.topcoder.com/blog/single-round-match-733-editorials/
@see https://community.topcoder.com/stat?c=round_overview&rd=17140
"""

import itertools


class MinimizeAbsoluteDifferenceDiv2():

    def findTriple(self, x0, x1, x2):

        originalList = [x0, x1, x2]
        result = (0, 1, 2)

        permutations = list(itertools.permutations(result))
        minFound = abs(originalList[0] / float(originalList[1]) - originalList[2])

        for p in permutations:
            iterMin = abs(originalList[p[0]] / float(originalList[p[1]]) - originalList[p[2]])
            if iterMin < minFound:
                minFound = iterMin
                result = p

        return result
