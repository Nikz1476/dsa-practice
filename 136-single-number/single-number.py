class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # brute force, time - O(n), space = O(n)
        # freq = {}    
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
    
        # for num in freq:
        #     if freq[num] == 1:
        #         return num

        # #optimal, time - O(n), space -O(1)
        result = 0    
        for num in nums:
            result ^= num
    
        return result