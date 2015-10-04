__author__ = 'responsible'
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for item in board:  # check every row
            row = filter(lambda x: x != ".", item)
            if len(set(row)) != len(row):
                return False
        for item in [map(lambda x: x[i], board) for i in xrange(9)]:  # check every column
            column = filter(lambda x: x != ".", item)
            if len(set(column)) != len(column):
                return False
        for row in xrange(3):  # check every 3x3 square
            for column in xrange(3):
                square = board[row * 3][column * 3:column * 3 + 3] + board[row * 3 + 1][column * 3:column * 3 + 3] + board[row * 3 + 2][column * 3:column * 3 + 3]
                square = filter(lambda x: x != ".", square)
                if len(set(square)) != len(square):
                    return False
        return True