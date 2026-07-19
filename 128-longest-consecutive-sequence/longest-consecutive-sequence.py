class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #O(n),O(n)
        num_set = set(nums)
        longest = 0

        for num in num_set:

            # Is this the beginning of a sequence?
            if num - 1 not in num_set:

                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest