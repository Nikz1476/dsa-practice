#from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True

        # return False

        last_seen = {}

        for i, num in enumerate(nums):

            if num in last_seen:
                if i - last_seen[num] <= k:
                    return True

            last_seen[num] = i

        return False
        
        