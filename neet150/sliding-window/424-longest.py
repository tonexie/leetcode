class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        charHash = {}
        l, r = 0, 0
        output = 0
        
        while r < len(s):
            charHash[s[r]] = 1 + charHash.get(s[r], 0)
            freq = 0
            for value in charHash.values():
                freq = max(freq, value)
            length = r - l + 1
            if length - freq > k:
                charHash[s[l]] = charHash[s[l]] - 1
                l += 1
            else:
                output = max(length, output)
            r += 1
        return output
    
sol= Solution()
s = "ABCDEF"
k = 2
print(sol.characterReplacement(s, k))