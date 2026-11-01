class Solution:
    def minMoves(self, nums: list[int]) -> int:
        #O(n),O(1)
        sums = 0
        minimum = min(nums)
        for i in range(len(nums)):
            sums += nums[i] - minimum
        return sums

        
