# -*- encoding: utf-8 -*-

"""
SRM 731 - Div 2 (250) - RingLex

@see No editorial found
@see https://community.topcoder.com/stat?c=round_overview&er=5&rd=17095
"""

class RingLex():

    def getmin(self, s):

        n = len(s)
        generatedStr = ''

        # Partial use of Eratosthenes Algorithm
        # @see https://stackoverflow.com/questions/26561654/prime-numbers-less-than-or-equal-to-n
        for p in range(2, n):

            prime = True
            for j in range(2, p):
                if p % j == 0:
                    prime = False
                    break

            if not prime:
                continue

            # Get the minimum, uses "%" to get the asocciated periodicity
            for j in range(n):

                toCompare = ''
                for k in range(n):
                    toCompare += s[(j + p*k) % n]

                if not generatedStr or toCompare < generatedStr:
                    generatedStr = toCompare


        return generatedStr

