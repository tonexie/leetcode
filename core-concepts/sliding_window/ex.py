# Given a string s and an integer k, 
# find the length of the longest substring that contains at most k distinct characters.
from collections import defaultdict


s = "eceba"
k = 2

def substring(s, k):
  l, r, maxSub = 0, 0, 0
  char_count = defaultdict(int)
  
  while r < len(s):
    char_count[s[r]] += 1
    
    while len(char_count) > k:
      char_count[s[l]] -= 1
      if char_count[s[l]] == 0:
        del char_count[s[l]]
      l += 1
      
    maxSub = max(maxSub, r - l + 1)
    r += 1
  
  return maxSub

print(substring(s, k))