class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force 
        # time - O(n^2)
        # space - O(1)
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        # optimal - hashmap 
        # time, space - O(n)
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i