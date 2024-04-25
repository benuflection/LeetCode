class Solution:
    def __init__(self, height):
        self.height = height
    def maxArea(self, height):

        res = 0
        l, r = 0 , len(height) - 1
        while l < r:
            curArea = min(height[l], height[r]) * abs(l - r)
            res = max(res, curArea)
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        return res
height = [1,8,6,2,5,4,8,3,7]
solution = Solution(height)
print(solution.maxArea(height))