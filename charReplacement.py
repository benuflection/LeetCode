class Solution:
    def __init__(self, s, k):
        self.s = s
        self.k = k
    def characterReplacement(self, s, k):


        res = 0
        l = 0
        count = {} #empty hash map to  store [letter,how many of that letter]

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)     #checks if letter at s[r] is in count and increments one
                                                        #if there are none of that letter it returns a default of zero and adds one
            while (r - l + 1) - max(count.values()) > k:  #while loop again acts as an if statement to move the left pointer
                count[s[l]] -= 1              #if length of window - largest count letter is > k
                l += 1               #it moves the left pointer right and decrements char at its old position

            res = max(res, r - l + 1)     # res updates at each iteration of the for loop
        return res                     #res has the largest valid window stored in it
s = "AABABBA"
k = 1
solution = Solution(s, k)
print(solution.characterReplacement(s, k))