class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # #brute force time - O(n^2), space = O(1)
        # n = len(nums)
        # max_count = 0

        # for i in range(n):
        #     count = 0
        #     for j in range(i, n):
        #         if nums[j] == 1:
        #             count += 1
        #             max_count = max(max_count, count)
        #         else:
        #             break

        # return max_count

        #optimal - using running counter 
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count

        #both time and space complexity O(n) and O(1)

        # left = 0
        # max_len = 0

        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         left = right + 1
        #     else:
        #         max_len = max(max_len, right - left + 1)

        # return max_len
