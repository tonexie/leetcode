class Solution:

    def __init__(self) -> None:
        self.d = ";"

    def encode(self, strs):
        if len(strs) == 0:
            return self.d.join(strs)
        return self.d.join(strs) + self.d

    def decode(self, s):
        decodeList = []
        curr = ""
        for i, c in enumerate(s):
            if c != self.d:
                curr = curr + c
            else:
                decodeList.append(curr)
                curr = ""
        return decodeList
      
      
# neet
class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # finds the number before the delimiter 
            length = int(s[i:j])
            i = j + 1
            j = i + length
            # finds the string after the delimiter 
            res.append(s[i:j])
            i = j
            
        return res



solution = Solution()
input = [""]
encoded = solution.encode(input)
decoded = solution.decode(encoded)

print(encoded)
print(decoded)
