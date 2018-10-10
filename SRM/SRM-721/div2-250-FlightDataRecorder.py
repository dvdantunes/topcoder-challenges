# -*- encoding: utf-8 -*-

"""
SRM 721 - Div 2 (250) - FlightDataRecorder

@see https://www.topcoder.com/blog/single-round-match-721-editorials/
@see https://community.topcoder.com/stat?c=problem_statement&pm=14711&rd=16983
"""

import math


class FlightDataRecorder():

    def getDistance(self, heading, distance):

        coordinates = [0, 0]
        for i in range(len(heading)):

            newPoint = [distance[i] * math.cos(math.radians(heading[i])),
                        distance[i] * math.sin(math.radians(heading[i]))]
            coordinates = [coordinates[0] + newPoint[0],
                           coordinates[1] + newPoint[1]]

        return math.hypot(coordinates[0], coordinates[1])
