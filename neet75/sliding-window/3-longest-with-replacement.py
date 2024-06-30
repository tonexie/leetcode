class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charHash = {}
        maxSub = 0
        l = 0
        maxCount = 0

        for r, char in enumerate(s):
            if char in charHash:
                charHash[char] += 1
            else:
                charHash[char] = 1

            maxCount = max(maxCount, charHash[char])
            
            while r - l + 1 > maxCount + k:
                charHash[s[l]] -= 1
                l += 1
            
            maxSub = max(maxSub, r - l + 1)

        return maxSub

s = "BAAABBCCACB"
k = 3
sol = Solution()
print(sol.characterReplacement(s, k))
