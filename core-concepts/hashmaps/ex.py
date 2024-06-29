# Given an array of strings, group the anagrams together. 
# An anagram is a word or phrase formed by rearranging the 
# letters of a different word or phrase, typically using all 
# the original letters exactly once.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_ana(words):
  anagrams = {}
  
  for word in words:
    sort = f'{sorted(word)}'
    print(sort)
    if sort in anagrams:
      anagrams[sort].append(word)
    else:
      anagrams[sort] = [word]
      
  return list(anagrams.values())

print(group_ana(words))
      