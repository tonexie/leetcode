import random

class RandomizedSet(object):

    def __init__(self):
        self.index = {}
        self.array = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index: 
          return False
        else: 
          self.array.append(val)
          self.index[val] = len(self.array) - 1
          return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index: 
          i = self.index[val]
          self.index[self.array[-1]] = i
          self.array[i] = self.array[-1]
          self.index.pop(val)
          self.array.pop()
          return True
        else: 
          return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()