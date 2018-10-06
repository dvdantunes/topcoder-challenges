# -*- encoding: utf-8 -*-

"""
SRM 729 - Div 2 (250) - BrokenChessboard

@see No editorial found
@see https://community.topcoder.com/stat?c=problem_statement&pm=14785&rd=17082
"""

class BrokenChessboard():

    def mininumFixes(self, board):

        def bestRowWithMinimuFixes(board):

            for i in range(len(board)):



        boardBeginsWith = board[0][0]

        def getSquareColor(x, y, boardBeginsWith):

            firstRowBeginsWith = boardBeginsWith
            secondRowBeginsWith = "W" if firstRowBeginsWith == "B" else "B"

            rowBeginsWith = firstRowBeginsWith if x % 2 == 0 else secondRowBeginsWith
            rowSecondColor = "W" if rowBeginsWith == "B" else "B"

            return rowBeginsWith if y % 2 == 0 else rowSecondColor


        neededChanges = 0
        for i in range(len(board)):
            for j in range(len(board[0])):

                expectedColor = getSquareColor(i, j, boardBeginsWith)
                if board[i][j] != expectedColor:
                    neededChanges += 1


        return neededChanges


