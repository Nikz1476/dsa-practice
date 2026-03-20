class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # # brute force, time - O(log n)^2, space - O(logn n)
        # binary = bin(num)[2:]
        # flipped = ""
        # for bit in binary:
        #     if bit == '0':
        #         flipped += '1'
        #     else:
        #         flipped += '0'
    
        # return int(flipped, 2)

        # #better, time - O(logn), space - O(1)
        # mask = 1
        # while mask<=num:
        #     mask = mask << 1
        # mask = mask -1

        # return mask ^ num

        # optimal, time and space - O(1)
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
