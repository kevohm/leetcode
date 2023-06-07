class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        val = {'(':')','{':'}', '[':']',')':'(','}':'{', ']':'['}
        arr = ['(',')','{','}','[',']']
        stack = {}
        current = 0
        for j,i in enumerate(s):
            if i in arr:
                if i in stack.keys():
                    if stack[i] == arr[current]:
                        del stack[i]
                    else:
                        break
                else:
                    current = j
                    stack[val[i]] = i
        print(stack, current)
        return len(stack.keys()) == 0

obj = Solution()
obj.isValid("ads()]")
obj.isValid("ads([)]")