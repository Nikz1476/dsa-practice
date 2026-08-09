class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = nums[i] + prefix[i]
        total = prefix[n]
        for i in range(n):
            leftsum = prefix[i]
            rightsum = total - prefix[i+1]
            if leftsum == rightsum:
                return i
        return -1


        #O(n),O(1)
        # n = len(nums)
        # total = sum(nums)
        # leftsum = 0
        # for i in range(n):
        #     rightsum = total - nums[i] - leftsum
        #     if leftsum == rightsum:
        #         return i
        #     leftsum+=nums[i]
        # return -1