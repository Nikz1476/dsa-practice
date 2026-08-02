class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(n),O(n)
        # n = len(nums)
        # prefix = [1]*n
        # suffix = [1]*n
        # ans = [1]*n
        # for i in range(1,n):
        #     prefix[i] = prefix[i-1] * nums[i-1]
        # suffix[n-1] = 1
        # for i in range(n-2,-1,-1):
        #     suffix[i] = suffix[i+1] * nums[i+1]
        # for i in range(n):
        #     ans[i] = prefix[i]*suffix[i]
        # return ans

        #O(n),O(1)
        n = len(nums)
        ans = [1] * n

        # Prefix products
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        # Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans