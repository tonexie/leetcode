class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minSub = [0, float("inf")]
        l = 0
        tHash = {}

        for c in t:
            tHash[c] = tHash.get(c, 0) + 1

        for r, c in enumerate(s):
            if c in tHash:
                tHash[c] -= 1
            while max(tHash.values()) <= 0:
                if r - l < minSub[1] - minSub[0]:
                    minSub[0] = l
                    minSub[1] = r
                l += 1
                if s[l - 1] in tHash:
                    tHash[s[l - 1]] += 1
                    if tHash[s[l - 1]] > 0:
                        break

        if minSub[1] == float("inf"):
            return ""
        return s[minSub[0] : minSub[1] + 1]


s = "X"
t = "XY"
sol = Solution()
print(sol.minWindow(s, t))
