class Solution(object):
  def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    previous = ""
    total = 0
    
    for char in reversed(s):
      if char == 'I': total += 1
      elif char == 'V': total += 5
      elif char == 'X': total += 10
      elif char == 'L': total += 50
      elif char == 'C': total += 100
      elif char == 'D': total += 500
      elif char == 'M': total += 1000
      
      if char == 'I' and previous == 'V': total -= 2
      elif char == 'I' and previous == 'X': total -= 2
      elif char == 'X' and previous == 'L': total -= 20
      elif char == 'X' and previous == 'C': total -= 20
      elif char == 'C' and previous == 'D': total -= 200
      elif char == 'C' and previous == 'M': total -= 200
      
      previous = char
      
    return total
   
solution = Solution()
s = "MCMXCIV"
print(solution.romanToInt(s))