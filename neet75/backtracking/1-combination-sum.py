from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def checkSum(currIdx, comb, total):
            if total ==  target:
                res.append(comb[:])
                return
            
            if total > target or currIdx >= len(candidates):
                return
            
            checkSum(currIdx, comb + [candidates[currIdx]], total + candidates[currIdx])
            checkSum(currIdx + 1, comb, total)
        
        checkSum(0, [], 0)
        return res
    