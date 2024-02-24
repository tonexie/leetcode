class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
      
            
        l = 0
        r = len(s) - 1
        
        if len(s) > 0 :
          while (l < r and l != r):
            if not (s[l].isdigit() or s[l].isalpha()):
              l += 1
              continue
            elif not (s[r].isdigit() or s[r].isalpha()):
              r -= 1
              continue
            elif s[l].lower() != s[r].lower():
              return False
            l += 1
            r -= 1
        
        return True
            

solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))