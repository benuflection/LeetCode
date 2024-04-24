def containsDuplicate(self, nums):
    s = set(nums)
    return len(s) < len(nums)
nums = [1,2,3,1]
print(containsDuplicate(nums, nums))