class Solution:
    def longestPalindrome(self, s: str) -> str:
    # brute force, time - O(n^3), space - O(n)
    # n = len(s)
    # longest = ""
    
    # for i in range(n):
    #     for j in range(i, n):
    #         substring = s[i:j+1]
    #         if substring == substring[::-1]:  # check palindrome
    #             if len(substring) > len(longest):
    #                 longest = substring
                    
    # return longest

    #better, time - O(n^2), space O(1)
        # def expand(left, right):
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return s[left+1:right]

        # longest = ""
    
        # for i in range(len(s)):
        # # Odd length
        #     temp1 = expand(i, i)
        # # Even length
        #     temp2 = expand(i, i+1)
        
        #     if len(temp1) > len(longest):
        #         longest = temp1
        #     if len(temp2) > len(longest):
        #         longest = temp2

        # return longest

        #optimal Dp , time, space O(n^2)
    #     n = len(s)
    #     dp = [[False]*n for _ in range(n)]
    
    #     start = 0
    #     max_len = 1
    
    # # Single characters
    #     for i in range(n):
    #         dp[i][i] = True
    
    # # Check substrings
    #     for length in range(2, n+1):
    #         for i in range(n - length + 1):
    #             j = i + length - 1
            
    #             if s[i] == s[j]:
    #                 if length == 2 or dp[i+1][j-1]:
    #                     dp[i][j] = True
                    
    #                     if length > max_len:
    #                         start = i
    #                         max_len = length
    
    #     return s[start:start+max_len]

    #most optimal - Manacher algorithm, time,space - O(n)
    # Transform string
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        center = right = 0
    
        for i in range(n):
            mirror = 2*center - i
        
            if i < right:
                p[i] = min(right - i, p[mirror])
        
            # Expand
            a = i + p[i] + 1
            b = i - p[i] - 1
        
            while a < n and b >= 0 and t[a] == t[b]:
                p[i] += 1
                a += 1
                b -= 1
        
        # Update center
            if i + p[i] > right:
                center = i
                right = i + p[i]
    
    # Find max
        max_len = max(p)
        center_index = p.index(max_len)
    
        start = (center_index - max_len) // 2
        return s[start:start + max_len]