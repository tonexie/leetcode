class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minSub = [0, float("inf")]
        l = 0
        tHash = {}
        cHash = {}

        for c in t:
            tHash[c] = tHash.get(c, 0) + 1

        have = 0
        need = len(tHash)
        for r, c in enumerate(s):
            if c in tHash:
                cHash[c] = cHash.get(c, 0) + 1
                if cHash[c] == tHash[c]:
                    have += 1
            while have >= need:
                if r - l < minSub[1] - minSub[0]:
                    minSub[0] = l
                    minSub[1] = r
                l += 1
                if s[l - 1] in cHash:
                    cHash[s[l - 1]] -= 1
                    if cHash[s[l - 1]] < tHash[s[l - 1]]:
                        have -= 1
                        print(r)
                        print(cHash)

        if minSub[1] == float("inf"):
            return ""
        return s[minSub[0] : minSub[1] + 1]


s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s, t))
