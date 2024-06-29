from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        heap = []
        res = []
        heapq.heapify(heap)
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        for key, val in hashMap.items():
            heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)

        for item in heap:
            res.append(item[1])

        return res


nums = [1, 2, 2, 3, 3, 3]
k = 2

sol = Solution()
print(sol.topKFrequent(nums, k))
