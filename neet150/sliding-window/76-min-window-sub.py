# neet
class Solution:
    def minWindow(self, s, t):
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""




# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         tHash = {}
#         winHash = {}
#         output = ""
#         for c in t:
#             tHash[c] = 1 + tHash.get(c, 0)
#         l = 0

#         for r, c in enumerate(s):
#             winHash[c] = 1 + winHash.get(c, 0)
#             isSub = True
#             for k, v in winHash.items():
#                 if k not in tHash or v < tHash[k]:
#                     isSub = False
#                     break
#             if isSub:
#                 while True:
#                   if winHash[s[l]] - 1 >= tHash[s[l]]:
#                     l += 1
                  
#                   break
#                 substr = s[l : r + 1]
#                 if len(substr) < len(output) or len(output) == 0:
#                     output = substr
#         return output

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s, t))