class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = set('qwertyuiopasdfghjklzxcvbnm1234567890')
        characters = [char for char in s.lower() if char in alphanum]
        return characters == characters[::-1]