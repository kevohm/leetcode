nums = [2,7,11,15]
target = 9

def get_sum(nums, target):
    nums=sorted(nums)
    for i in range(len(nums)):
        if (nums[i] > target):
            break
        for j in range(len(nums)):
            if i != j and nums[j] + nums[i] == target:
                return [i,j]
    return None
print(get_sum(nums,target))