class Solution:
    def __init__(self, s):
        self.s = s
    def isPalindrome(self, s):

        s = s.lower()
        s = ''.join([char for char in s if char.isalnum()])
        l = list(s)
        for i in range(len(s)):
            if s[i] != s[-i - 1]:
                return False
        return True

s = "A man, a plan, a canal: Panama"
solution = Solution(s)
print(solution.isPalindrome(s))