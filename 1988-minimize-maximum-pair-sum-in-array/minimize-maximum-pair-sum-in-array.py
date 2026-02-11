class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        #optimal time - O(n logn)
        nums.sort()
        left = 0
        right = len(nums) - 1
        max_pair = 0
    
        while left < right:
            pair_sum = nums[left] + nums[right]
            max_pair = max(max_pair, pair_sum)
            left += 1
            right -= 1
    
        return max_pair