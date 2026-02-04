class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # time - O(n^2)
        # space - O(1)
        # n = len(nums)

        # for i in range(n + 1):
        #     found = False
        #     for num in nums:
        #         if num == i:
        #             found = True
        #             break

        #     if not found:
        #         return i

        # Better - hashset
        #time, space - O(n)
        # s = set(nums)
        # n = len(nums)

        # for i in range(n + 1):
        #     if i not in s:
        #         return i

        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum
        # time - O(n)
        # space - O(1)