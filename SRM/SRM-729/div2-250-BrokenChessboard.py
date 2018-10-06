# -*- encoding: utf-8 -*-

"""
SRM 729 - Div 2 (250) - BrokenChessboard

@see No editorial found
@see https://community.topcoder.com/stat?c=problem_statement&pm=14785&rd=17082
"""

class BrokenChessboard():

    def mininumFixes(self, board):

        def getSquareColor(x, y, boardBeginsWith):

            firstRowBeginsWith = boardBeginsWith
            secondRowBeginsWith = "W" if firstRowBeginsWith == "B" else "B"

            rowBeginsWith = firstRowBeginsWith if x % 2 == 0 else secondRowBeginsWith
            rowSecondColor = "W" if rowBeginsWith == "B" else "B"

            return rowBeginsWith if y % 2 == 0 else rowSecondColor


        neededChanges1 = 0
        neededChanges2 = 0
        for i in range(len(board)):
            for j in range(len(board[0])):

                expectedColor = getSquareColor(i, j, 'W')
                if board[i][j] != expectedColor:
                    neededChanges1 += 1

                expectedColor = getSquareColor(i, j, 'B')
                if board[i][j] != expectedColor:
                    neededChanges2 += 1


        return min(neededChanges1, neededChanges2)


