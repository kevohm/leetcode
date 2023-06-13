class Solution(object):
    def find_if_fascinating(self, n):
        s = 2 * n
        c = 3 * n
        final = str(n) + str(s) + str(c)
        return self.check_num(final)
    
    def check_num(self, num):
        check = True
        arr = []
        for i in str(num):
            if i == "0":
                return False
            if i not in arr:
                arr.append(i)
            else:
                return False
        return check
print(Solution().find_if_fascinating(111))