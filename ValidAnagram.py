class Solution:
    def __init__(self, s, t):
        self.s = s
        self.t = t
    def isAnagram(self, s, t):
    # sorted() will sort the chars of a string by ascii value or ints least to greatest
        return sorted(s) == sorted(t)
s = "anagram"
t = "nagaram"
solution = Solution(s, t)
print(solution.isAnagram(s, t))