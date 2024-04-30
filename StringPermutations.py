class Solution:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        # Count frequencies of characters in s1
        for char in s1:
            s1Count[ord(char) - ord('a')] += 1

        # Iterate through s2 with a sliding window
        for i in range(len(s2)):
            # Increment the count of the current character in s2
            s2Count[ord(s2[i]) - ord('a')] += 1

            # Check if the sliding window size is greater than s1
            if i >= len(s1):
                # Decrement the count of the character leaving the window
                s2Count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # If the frequency counts match for all characters, return True
            if s1Count == s2Count:
                return True

        return False
s1 = "ab"
s2 = "eidbaooo"
solution = Solution(s1, s2)
print(solution.checkInclusion(s1, s2))