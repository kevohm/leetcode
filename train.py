
class Sort(object):
    def __init__(self, search=[1,2,3,4,5,6,7,8,9], sort=[9,8,7,6,5,4,3,2,1]) -> None:
        self.arr_search = search
        self.arr_sort = sort
    def binary_search(self, s) -> int:
        arr = self.arr_sort
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if arr[mid] < s:
                left = mid + 1
            elif arr[mid] > s:
                right = mid - 1
            else:
                return arr[mid]
        return -1
    def linear_search(self, s) -> int:
        arr = self.arr_search
        for i in arr:
            if i == s:
                return i
        return -1
    def bubble_sort(self):
        arr = self.arr_sort
        for j in range(0, len(arr)):
            for i in range(len(arr) - j - 1):
                temp = 0
                if arr[i] > arr[i + 1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
        return self.arr_sort
    def selection_sort(self):
        arr = self.arr_sort
        current = 0
        min_val = 0
        while current < len(arr) - 1:
            for i in range(current,len(arr)):
                if arr[i] < arr[min_val]:
                    min_val = i
            if arr[min_val] < arr[current]:
                arr[current], arr[min_val] = arr[min_val], arr[current]
            current += 1
        return arr
            
obj = Sort()
print(obj.selection_sort())
