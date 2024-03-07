import collections

# my solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        paraStack = collections.deque()

        for i in range(len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                paraStack.append(s[i])
            elif s[i] == "}" and paraStack and paraStack[-1] == "{":
                paraStack.pop()
            elif s[i] == "]" and paraStack and paraStack[-1] == "[":
                paraStack.pop()
            elif s[i] == ")" and paraStack and paraStack[-1] == "(":
                paraStack.pop()
            else:
                return False

        if paraStack:
            return False
        return True
      
# after solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        paraStack = collections.deque()
        for c in s:
          if c == "(":
            paraStack.append(")")
          elif c == "[":
            paraStack.append("]")
          elif c == "{":
            paraStack.append("}")
          elif not paraStack or c != paraStack.pop():
            return False
        
        return not paraStack

sol = Solution()
s = "[]"
print(sol.isValid(s))
