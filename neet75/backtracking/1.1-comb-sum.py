from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(currArr, currIdx, sum):
            if sum == target:
                res.append(currArr)
                return
            if sum > target or currIdx > len(candidates):
                return
            dfs(currArr + [candidates[currIdx]], currIdx, sum + candidates[currIdx])
            dfs(currArr, currIdx + 1, sum)
        dfs([], 0, 0)
        return res
