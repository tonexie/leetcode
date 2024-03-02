class Solution(object):
    def checkInclusion(self, s1, s2):
        s1Array = [0] * 26
        for c in s1:
            index = ord(c) - ord("a")
            s1Array[index] += 1
        
        window = [0] * 26
        l = 0
        for i, r in enumerate(s2):
            window[ord(r) - ord("a")] += 1
            if i >= len(s1):
                window[ord(s2[l]) - ord("a")] -= 1
                l += 1
            if s1Array == window:
                return True
        
        return False



# core idea here is to store counts in a 26 index list for the letters, and then compare if they are the same
class Solution(object):
    def checkInclusion(self, s1, s2):
        s1Set = set()
        s1Counts = [0] * 26
        for c in s1:
            s1Counts[ord(c) - ord("a")] += 1
        s1Set.add(tuple(s1Counts))
        
        for r in range(len(s2) - len(s1) + 1):
            sub = [0] * 26
            for i in range(len(s1)):
                sub[ord(s2[i + r]) - ord("a")] += 1

            if tuple(sub) in s1Set:
                return True
            
        return False

# the above, but sliding window
class Solution(object):
    def checkInclusion(self, s1, s2):
        s1Counts = [0] * 26
        for c in s1:
            s1Counts[ord(c) - ord("a")] += 1
        
        windowCounts = [0] * 26
        for i in range(len(s2)):
            # Add the new character to the window counts
            windowCounts[ord(s2[i]) - ord("a")] += 1
            
            # If the window size exceeds the length of s1, remove the character at the start of the window
            if i >= len(s1):
                windowCounts[ord(s2[i - len(s1)]) - ord("a")] -= 1
            
            # Compare the counts of characters in the current window with s1
            if windowCounts == s1Counts:
                return True
            
        return False




sol = Solution()
s1 = "ab"
s2 = "eiasdbasdf"
print(sol.checkInclusion(s1, s2))
