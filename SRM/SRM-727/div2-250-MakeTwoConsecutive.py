# -*- encoding: utf-8 -*-

"""
SRM 727 - Div 2 (250) - MakeTwoConsecutive

@see No editorial found
@see https://community.topcoder.com/stat?c=round_overview&er=5&rd=17055
"""

class MakeTwoConsecutive():

    def solve(self, S):

        for i in range(len(S)):

            # No need to remove?
            if (i+1) < len(S) and S[i] == S[i+1]:
                return "Possible"

            # Removing 2nd element from a chunk of 3, comparing the now adjacents
            chunk = S[i : i+3 : 2]
            if len(chunk) == 2 and len(set(chunk)) == 1:
                return "Possible"

        return "Impossible"
