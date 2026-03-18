class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # #brute force, time - O(logn) space - O(1)
        # count = 0    
        # while n > 0:
        #     if (n & 1) == 1:
        #         count += 1
        #     n = n >> 1
        # return count

        # #Optimal (Brian Kernighan Algorithm) 
        count = 0 
        while n:
            n = n & (n-1)
            count +=1
        return count
        # time - O(number of set bits)
        # worst - O(logn)
        #space - O(1) 
        