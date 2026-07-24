class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # #O(n), O(1) - optimized
        if (n<=2):return n
        
        p2 = 1 
        p1 = 2 
        for _ in range(3,n+1):
            curr = p1 + p2
            p2 = p1
            p1 = curr
        
        return p1


        #O(n),O(n) - DP array
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        #O(n),O(n) 
        # memo = {}

        # def dfs(i):
        #     if i <= 2:
        #         return i

        #     if i not in memo:
        #         memo[i] = dfs(i - 1) + dfs(i - 2)

        #     return memo[i]

        # return dfs(n)