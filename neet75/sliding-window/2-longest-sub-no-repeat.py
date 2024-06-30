class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        maxSub = 0
        l = 0

        for char in s:
            while char in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(char)
            maxSub = max(len(hashSet), maxSub)

        return maxSub


s = "zxyzxyz"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
