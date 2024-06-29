from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for str in strs:
            charList = [0] * 26
            for c in str:
                charList[ord(c) - ord("a")] += 1
            charKey = tuple(charList)
            hashMap[charKey] = hashMap.get(charKey, [])
            hashMap[charKey].append(str)

        return list(hashMap.values())


strs = ["act", "pots", "tops", "cat", "stop", "hat"]

sol = Solution()
print(sol.groupAnagrams(strs))
