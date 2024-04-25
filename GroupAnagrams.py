
class Solution:
    def __init__(self, strs):
        self.strs = strs
    def groupAnagrams(self, strs):

        def AnKey(string):
            key = ''
            for w in sorted(string):
                key += w
            return str(key)

        def Grouper(strs):
            group = dict()
            for str in strs:
                if group.get(AnKey(str)) == None:
                    group[AnKey(str)] = [str]
                else:
                    group[AnKey(str)].append(str)
            return group

        Anagrams = Grouper(strs)
        AnagramsFinal = list()
        for i, j in Anagrams.items():
            AnagramsFinal.append(j)
        return AnagramsFinal

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution(strs)
print(solution.groupAnagrams(strs))