class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        length = 0
        charHash = {}
        if s:
            charHash[s[l]] = 0
            length = 1
        for i in range(len(s) - 1):
            r = i + 1
            print(s[i])
            if s[r] not in charHash:
                charHash[s[r]] = r
            else:
                length = max(length, r - l)
                l = charHash[s[r]] + 1
                charHash[s[r]] = r
            length = max(length, r - l)

        return length

# my solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        length = 0
        charHash = {}
        for r in range(len(s)):
          # check if char has been repoeated yet and ensures r > L
            if s[r] in charHash and charHash[s[r]] >= l:
                l = charHash[s[r]] + 1
            charHash[s[r]] = r
            length = max(length, r - l + 1)
        return length
    
# neet + me
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        l = 0
        length = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            length = max(length, r - l + 1)

        return length

sol = Solution()
s = "abcadcbba"
print(sol.lengthOfLongestSubstring(s))
