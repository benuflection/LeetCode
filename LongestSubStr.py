class Solution:
    def __init__(self, s):
        self.s = s
    def lengthOfLongestSubstring(self, s):

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:  #while loop acts like an "if" statement and will only run if char at r pointer is in the set
                charSet.remove(s[l]) #if it is, it removes characters from the left and moves the left pointer until the rth char is not in the set
                l += 1
            charSet.add(s[r])         #rth char is added to the set and distance between pointers is measured
            res = max(res, r - l + 1)
        return res
s = "abcabcbb"
solution = Solution(s)
print(solution.lengthOfLongestSubstring(s))