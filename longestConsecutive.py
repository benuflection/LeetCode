class Solution:
    def __init__(self, nums):
        self.nums = nums
    def longestConsecutive(self, nums):

        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
nums = [100, 4, 200, 1, 3, 2]
solution = Solution(nums)
print(solution.longestConsecutive(nums))