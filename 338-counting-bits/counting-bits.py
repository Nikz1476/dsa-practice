class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # # brute force, time - O(n log n), space - O(1)
        # def count_ones(x):
        #     count = 0
        #     while x:
        #         x = x & (x - 1)
        #         count += 1
        #     return count

        # return [count_ones(i) for i in range(n + 1)]

        # # optimal, time - O(n), space - O(n)
        ans = [0] * (n + 1)    
        # for i in range(1, n + 1): right shift and removes the last bit
        #     ans[i] = ans[i >> 1] + (i & 1)
        #     ans[i] = ans[i // 2] + (i % 2)
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1
    
        return ans