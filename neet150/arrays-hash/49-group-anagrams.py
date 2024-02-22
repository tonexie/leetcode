# sorted str way
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hashStrs = {}
        output = []

        # put sorted str into a hashmap with list of its indexes
        for i, str in enumerate(strs):
            sortedStr = "".join(sorted(str))
            if sortedStr in hashStrs:
                hashStrs[sortedStr].append(i)
            else:
                hashStrs[sortedStr] = [i]

        # generate outpu
        for sortedStr in hashStrs:
            list = []
            output.append(list)
            for index in hashStrs[sortedStr]:
                list.append(strs[index])

        return output


# neet
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashList = dict()

        for s in strs:
            count = [0] * 26

            # key insight is to have the entire list be the key, so that i can match patterns easily
            for c in s:
                count[ord(c) - ord("a")] += 1

            if tuple(count) in hashList:
                hashList[tuple(count)].append(s)
            else:
                hashList[tuple(count)] = [s]

        return list(hashList.values())


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(solution.groupAnagrams(strs))
