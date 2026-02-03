class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n^2) solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):  
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        #O(n) - optimal
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False