class Solution:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
    def twoSum(self, numbers, target):

        l = 0
        r = len(numbers) - 1
        while l < r:  # handles overlapping l and r values

            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
numbers = [2,7,11,15]
target = 9
solution = Solution(numbers, target)
print(solution.twoSum(numbers, target))