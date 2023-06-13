class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr = {}
        arr_b = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a in arr.keys():
                arr[a] = arr[a] + 1
            else:
                arr[a] = 1
            if b in arr_b.keys():
                arr_b[b] += 1
            else:
                arr_b[b] = 1
        for i in arr:
            if arr.get(i) != arr_b.get(i):
                return False
        return True
