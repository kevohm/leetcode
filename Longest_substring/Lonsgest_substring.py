
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = []
        arr = []
        for i in s:
            if i in arr:
                ans.append(arr)
                arr = []
                arr.append(i)
            else:
                arr.append(i)
        ans.append(arr)
        if len(ans) > 0:
            max = len(ans[0])
            data = ans[0]
            for i in range(len(ans)):
                l = len(ans[i])
                if l > max:
                    max = l
                    data = ans[i]
            print(data)
            return len(data)
        return len(arr)

Solution().lengthOfLongestSubstring("aab")