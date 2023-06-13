class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        ans = ""
        left = 0
        if l < 1:
            return s
        for i in range(1, l):
            diff = i - left - 1
            a = s[left:i]
            b = s[i-1:(i + diff)]
            print(str(a),str(b),a == b)
            if a == b and len(a) > len(ans):
                ans = a
        print(ans)

Solution().longestPalindrome("babad")