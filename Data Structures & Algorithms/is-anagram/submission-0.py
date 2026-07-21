class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted([c for c in s])
        str2 = sorted([c for c in t])
        return str1 == str2