class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        if len(s) > 0:
          while l <= r:
            while l <= r and not s[l].isalnum():
              l += 1
            while l <= r and not s[r].isalnum() :
              r -= 1
            if l > r:
              break
            if s[l].lower() != s[r].lower():
              return False
            l += 1
            r -= 1
        
        return True
      
s = " "
sol = Solution()
print(sol.isPalindrome(s))