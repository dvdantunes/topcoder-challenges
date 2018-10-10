# -*- encoding: utf-8 -*-

"""
SRM 718 - Div 2 (250) - RelativeHeights

@see https://www.topcoder.com/blog/single-round-match-718-editorials/
@see https://community.topcoder.com/stat?c=round_overview&er=5&rd=16933
"""

class RelativeHeights():

    def countWays(self, h):

        def getProfile(skyscraperList):

            original = skyscraperList.copy()
            skyscraperList.sort(reverse=True)

            profile = []
            for x in original:
                profile.append(skyscraperList.index(x))

            return profile


        numProfiles = 0
        profiles = []
        for i in range(len(h)):

            newProfile = getProfile(h[:i] + h[i+1:])
            if newProfile not in profiles:
                numProfiles += 1
                profiles.append(newProfile)

        return numProfiles
