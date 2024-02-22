class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashMap = {}
        output = []

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)

        sortedList = sorted(
            hashMap.items(), key=lambda item: item[1]
        )  # same as (item) => (item[i]), where item is the first argument, this means map is sorted by value

        for i in range(k):
            output.append(sortedList[-1 - i][0])

        return output

# my neet 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashMap = {}
        freq = [[] for i in range(len(nums))]
        output = []

        for n in nums:
          hashMap[n] = hashMap.get(n, 0) + 1
          
        for num, count in hashMap.items():
          freq[count - 1].append(num)
          
        for i in range(len(freq) - 1, -1, -1): #reverse loop
          for j in freq[i]:
            output.append(j)
            if len(output) == k:
              return output


solution = Solution()

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(solution.topKFrequent(nums, k))
