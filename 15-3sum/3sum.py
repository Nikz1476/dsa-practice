class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #Brute Force  -  O(n^3), O(number of triplets)
        # def threeSum(self, nums):
        # ans = set()
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        # return [list(x) for x in ans]

        
        #O(n^2),O(1)
        nums.sort()     
        res = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1

                elif total < 0:
                    l += 1

                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res