class Solution:
    def __init__(self, height):
        self.height = height
    def trap(self, height):

        if not height: return 0
        res = 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution(height)
print(solution.trap(height))