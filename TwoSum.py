class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for n in range(i + 1, len(nums)):
                if nums[i] + nums[n] == target:
                    result = [i,n]
                    break
        return result
nums = [2,7,11,15]
target = 9
solution = Solution(nums, target)
print(solution.twoSum(nums, target))