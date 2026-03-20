class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # # brute force, time - O(n^2), space - O(1)
        # max_length = 0
        # # Outer loop for starting index of substrings
        # for i in range(len(s)):
        #     # Array to track frequency of characters in window
        #     freq = [0] * 26
        #     # Variable to store the frequency of most common character in window
        #     max_freq = 0
        #     # Inner loop to go from current start to end of string
        #     for j in range(i, len(s)):
        #         # Increment count of current character
        #         freq[ord(s[j]) - ord('A')] += 1
        #         # Update max frequency seen so far
        #         max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])
        #         # Length of current window
        #         window_len = j - i + 1
        #         # Number of characters to replace
        #         replace = window_len - max_freq
        #         # Check if we can replace within k
        #         if replace <= k:
        #             max_length = max(max_length, window_len)
        # return max_length

        # # better, time - O(n), space - O(26)
        # freq = {}

        # # Left pointer of sliding window
        # left = 0

        # # Stores max frequency of any char in current window
        # max_freq = 0

        # # Stores result
        # max_len = 0

        # # Traverse through each character with right pointer
        # for right in range(len(s)):
        #     # Increase frequency of current character
        #     freq[s[right]] = freq.get(s[right], 0) + 1
        #     # Update the max frequency in current window
        #     max_freq = max(max_freq, freq[s[right]])

        #     # If window is invalid (more than k replacements)
        #     while (right - left + 1) - max_freq > k:
        #         freq[s[left]] -= 1
        #         left += 1

        #     # Update max_len with current valid window size
        #     max_len = max(max_len, right - left + 1)

        # return max_len

        # # optimal, time - O(n), space - O(1)

        freq = [0] * 26

        # Left pointer of sliding window
        left = 0

        # Tracks the count of the most frequent character in current window
        maxCount = 0

        # Stores the maximum length of valid window
        maxLength = 0

        # Iterate through the string with right pointer
        for right in range(len(s)):

            # Increment the frequency of current character
            freq[ord(s[right]) - ord('A')] += 1

            # Update maxCount with the max frequency seen so far
            maxCount = max(maxCount, freq[ord(s[right]) - ord('A')])

            # If the current window needs more than k replacements, move left
            while (right - left + 1) - maxCount > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            # Update the maximum window length
            maxLength = max(maxLength, right - left + 1)

        # Return the maximum valid window length
        return maxLength