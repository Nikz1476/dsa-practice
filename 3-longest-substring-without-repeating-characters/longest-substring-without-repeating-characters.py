class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # #brute force
        # #time - O(n^2), space - O(n)
        # n = len(s)
        # max_len = 0
    
        # for i in range(n):
        #     seen = set()
        #     for j in range(i, n):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         max_len = max(max_len, j - i + 1)
    
        # return max_len

        # #better -sliding window + set, time and space - O(n)
        # n = len(s)
        # char_set = set()
        # left = 0
        # max_len = 0
    
        # for right in range(n):
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1
        
        #     char_set.add(s[right])
        #     max_len = max(max_len, right - left + 1)
    
        # return max_len


        #optimal- sliding window + hashmap, time and space - O(N)
        char_map = {}
        left = 0
        max_len = 0
    
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
        
            char_map[char] = right
            max_len = max(max_len, right - left + 1)
    
        return max_len