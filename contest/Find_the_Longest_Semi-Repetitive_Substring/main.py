class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(self.find_semi(s))
        return len(self.find_semi(s))
    
    def find_semi(self, s):
        final = {}
        arr = []
        repeat = False
        if len(s) < 2:
            return s
        for i,j in enumerate(s):
            if j not in final.keys():
                if len(arr) > 2:
                    return s[:i+1]
                elif len(arr) <= 2 and i == len(s) - 1:
                    return s
                final[j] = i
            else:
                if j in arr and i == len(s) - 1:
                    return s[:i-1]
                elif j in arr:
                    return s[:i]
                else:
                    if i == len(s) - 1:
                        return s
                    else:
                        arr.append(j)

print(Solution().longestSemiRepetitiveSubstring("54422"))