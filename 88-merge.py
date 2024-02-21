class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1 #first set
        b = n - 1 #second set
        c = m + n - 1 

        while a >= 0 and b >= 0:
            if nums1[a] > nums2[b]:
                nums1[c] = nums1[a]
                a -= 1
            else:
                nums1[c] = nums2[b]
                b -= 1
            c -= 1
            
        while b >= 0:
            nums1[c] = nums2[b]
            b -= 1
            c -= 1

nums1 = [8,9,9,0,0,0]
m = 3
nums2 = [4,5,6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)

print(nums1)
