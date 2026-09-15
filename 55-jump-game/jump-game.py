class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy - O(n),O(1)
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i+nums[i])
        return True

        #DFS - O(2^n), O(n)
        # n = len(nums)
        # def dfs(i):
        #     if i >= n-1:
        #         return True
        #     for jump in range(1,nums[i]+1):
        #         if dfs(i+jump):
        #             return True
        #     return False
        # return dfs(0)



        #memoization - O(n^2),O(1)
        # n = len(nums)
        # memo = {}

        # def dfs(i):

        #     # Reached the end
        #     if i >= n - 1:
        #         return True

        #     # Already calculated
        #     if i in memo:
        #         return memo[i]

        #     # Try every possible jump
        #     for jump in range(1, nums[i] + 1):

        #         if dfs(i + jump):
        #             memo[i] = True
        #             return True

        #     # No jump worked
        #     memo[i] = False
        #     return False

        # return dfs(0)