class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) <= 1:
            return arr
        max = 0
        l = len(arr)
        for i in range(l):
            if i == l - 1:
                arr[i] = -1
                break
            max = i + 1
            for k in range(i + 1, l):
                if arr[k] > arr[max]:
                    max = k
            arr[i] = arr[max]
        return arr
obj =Solution()
print(obj.replaceElements([1,2,3,4,5,6,17,8,9]))
