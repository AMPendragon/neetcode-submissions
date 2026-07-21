class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        sublists = []
        i = 0
        for s in strs:
            d = tuple(sorted(s))
            if d not in seen:
                seen[d] = i
                i += 1
                sublists.append([s])
            else:
                sublists[seen[d]].append(s)
        return sublists