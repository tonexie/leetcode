class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """        
        rev_sorted = sorted(citations, reverse=True)
        h_index = rev_sorted[0]
        current_count = 0
        max_count = 0
        
        for i in range(len(rev_sorted)):
          if rev_sorted[i] > current_count :
            current_count += 1
          else:
            if current_count > h_index:
              current_count = h_index
            max_count = max(max_count, current_count)
            current_count = 0
            h_index = rev_sorted[i]

        return max(max_count, current_count)
            
           
citations = [1]            
solution = Solution()
print(solution.hIndex(citations))
        