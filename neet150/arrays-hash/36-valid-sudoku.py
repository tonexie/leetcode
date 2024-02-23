class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.checkRow(board) and self.checkCol(board) and self.checkGrid(board)
        
    def checkRow(self, board):
        for i in range(9):
            rSet = set()
            for j in range(9):
                cell = board[i][j]
                if cell != ".":
                    if cell in rSet:
                        return False
                rSet.add(cell)
        return True

    def checkCol(self, board):
        for i in range(9):
            cSet = set()
            for j in range(9):
                cell = board[j][i]
                if cell != ".":
                    if cell in cSet:
                        return False
                cSet.add(cell)
        return True

    def checkGrid(self, board):
        # grid row
        for i in range(0, 9, 3):

            # grid col
            for j in range(0, 9, 3):
                gSet = set()

                # sub row
                for k in range(3):

                    # sub col
                    for l in range(3):
                        cell = board[i + k][j + l]
                        if cell != ".":
                            if cell in gSet:
                                return False
                        gSet.add(cell)
        return True




solution = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "5", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(solution.isValidSudoku(board))
