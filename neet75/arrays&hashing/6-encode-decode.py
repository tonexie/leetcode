class Solution:
    def __init__(self) -> None:
        self.delim = ";"

    def encode(self, strs):
        if len(strs) == 1 and strs[0] == "":
          return ";"
        encoded = self.delim.join(strs)
        return encoded

    def decode(self, s):
        if not s:
            return []
        if s == ";":
            return [""]
        res = []
        currS = ""
        for c in s:
            if c != ";":
                currS += c
            else:
                res.append(currS)
                currS = ""
        res.append(currS)

        return res


str = [""]
sol = Solution()
print(sol.encode(str))
