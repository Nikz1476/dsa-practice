class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #O(n),O(1)
        left = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

        #O(nlogn)
        n = len(nums)

        # Build prefix sums
        # prefix = [0] * (n + 1)
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + nums[i]

        # ans = float('inf')

        # for i in range(n):
        #     required = prefix[i] + target
        #     j = bisect_left(prefix, required)

        #     if j <= n:
        #         ans = min(ans, j - i)

        # return 0 if ans == float('inf') else ans