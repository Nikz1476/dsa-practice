class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #O(n),O(n)
        prefix_count = defaultdict(int)
        prefix_count[0] = 1      # Empty prefix

        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            count += prefix_count[curr_sum - k]

            prefix_count[curr_sum] += 1

        return count

        #O(n^2) - brute force
        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     curr_sum = 0

        #     for j in range(i, n):
        #         curr_sum += nums[j]

        #         if curr_sum == k:
        #             count += 1

        # return count