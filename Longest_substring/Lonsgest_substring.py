class Solution(object):
    ans = []
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.recursive_search(s)
        len_arr = self.check_length(Solution.ans)
        Solution.ans = []
        return len_arr

    def recursive_search(self, s, i=0):
        if i >= len(s):
            return
        arr = []
        for k in range(0,len(s)):
            arr = []
            arr =  s[i:len(s) - k]
            if(len(arr) > 0):
                self.add_data(arr)
        self.recursive_search(s, i+1)
    
    def check_rep(self, s):
        arr = []
        if s is None:
            return None
        for i in s:
            if i in arr:
                return None
            arr.append(i)
        return arr
    
    def add_data(self, arr):
        array = self.check_rep(arr)
        if array is not None:
            if array not in Solution.ans:
                Solution.ans.append(array)
    
    def check_length(self, arr):
        if len(arr) < 1:
            return 0
        max = arr[0]
        for i in arr:
            if len(i) > len(max):
                max = i
        return len(max)