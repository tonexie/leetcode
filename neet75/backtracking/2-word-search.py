from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if (
                not 0 <= r < len(board)
                or not 0 <= c < len(board[0])
                or board[r][c] != word[idx]
                or idx >= len(word)
                or (r, c) in vis
            ):
                return False

            vis.add((r, c))
            res = (
                dfs(r + 1, c, idx + 1)
                or dfs(r - 1, c, idx + 1)
                or dfs(r, c + 1, idx + 1)
                or dfs(r, c - 1, idx + 1)
            )
            vis.remove((r, c))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False