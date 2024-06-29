class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charSet = set()
        tList = [0] * 26
        sList = [0] * 26
        for c in s.lower():
          sList[ord(c) - ord('a')] += 1
        charSet.add(tuple(sList))
        
        for c in t.lower():
          tList[ord(c) - ord('a')] += 1
          
        if tuple(tList) in charSet:
          return True
        else:
          return False
        
sol = Solution()
print(sol.isAnagram('racecar', 'carrace'))