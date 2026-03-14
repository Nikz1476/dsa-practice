class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        #brute force 
        n = int(s, 2)
        steps = 0
        
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n += 1
            steps += 1
        
        return steps
        # steps = 0
        # carry = 0
        
        # for i in range(len(s)-1, 0, -1):
        #     bit = int(s[i])
            
        #     if bit + carry == 1:
        #         steps += 2
        #         carry = 1
        #     else:
        #         steps += 1
        
        # return steps + carry