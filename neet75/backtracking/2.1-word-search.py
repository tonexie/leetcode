from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()

        def dfs(row, col, idx, currWord):
            if word == currWord:
                return True
            if (
                row >= len(board)
                or row < 0
                or col >= len(board[0])
                or col < 0
                or (idx < len(word) and board[row][col] != word[idx])
                or (row, col) in vis
            ):
                return False
            else:
                currWord += board[row][col]
            vis.add((row, col))
            if (
                dfs(row + 1, col, idx + 1, currWord)
                or dfs(row - 1, col, idx + 1, currWord)
                or dfs(row, col + 1, idx + 1, currWord)
                or dfs(row, col - 1, idx + 1, currWord)
            ):
                return True
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, ""):
                    return True
