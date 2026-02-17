class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # #brute force, time - O(n^2), space O(1)
        # n = len(nums)
        # max_sum = float('-inf')
    
        # for i in range(n):
        #     current_sum = 0
        #     for j in range(i, n):
        #         current_sum += nums[j]
        #         max_sum = max(max_sum, current_sum)
    
        # return max_sum

        # #tabulated, time and space O(n)
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # max_sum = dp[0]
    
        # for i in range(1, n):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])
        #     max_sum = max(max_sum, dp[i])
    
        # return max_sum


        #kadanes algorithm O(n)
        max_sum = nums[0]
        current_sum = nums[0]
    
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
    
        return max_sum