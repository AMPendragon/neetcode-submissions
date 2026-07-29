class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        ls = sorted(list(set(nums)))
        longest = 0
        counter = 1
        for i in range(1, len(ls)):
            if ls[i-1] == ls[i]-1:
                counter += 1
            else:
                if longest < counter:
                    longest = counter
                counter = 1
        if longest < counter:
            longest = counter
        return longest