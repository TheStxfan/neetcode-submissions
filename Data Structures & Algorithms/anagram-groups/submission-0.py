class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            res[sortedStr].append(s)
        return list(res.values())