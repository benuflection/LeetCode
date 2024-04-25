class Solution:
    def __init__(self, nums):
        self.nums = nums
    def containsDuplicate(self, nums):
        s = set(nums)
        return len(s) < len(nums)
nums = [1,2,3,1]
solution = Solution(nums)
print(solution.containsDuplicate(nums))