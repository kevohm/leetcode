class Solution(object):
    ans = {}
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #prevent objects using answers from previous objects
        length = self.recursiveSearch(s)
        Solution.ans = {}
        return length

    def recursiveSearch(self, s, i=0):
        current = 0
        obj = Solution.ans
        length = 0
        total = 0
        for i,j in enumerate(s):
            if j in obj.keys():
                if obj[j]+1 == i:
                    obj = {}
                    current = i
                elif obj[j] >= current:
                    current = obj[j] + 1
            obj[j] = i
            total = i - current + 1
            if length < total:
                length = total
        return length