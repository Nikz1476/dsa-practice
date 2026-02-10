class Solution:
    def reverseWords(self, s: str) -> str:
        #brute force
        # words = s.strip().split()
        # return " ".join(words[::-1])

        #time and space, above and below both methods - time,space - O(n)
        #better - manual parsing without split
        # res = []
        # i = len(s) - 1

        # while i >= 0:
        #     # skip spaces
        #     while i >= 0 and s[i] == ' ':
        #         i -= 1
        #     if i < 0:
        #         break

        #     j = i
        #     # find word
        #     while i >= 0 and s[i] != ' ':
        #         i -= 1

        #     res.append(s[i+1:j+1])

        # return " ".join(res)


        #optimal
        #time - O(n)
        #space -O(1)
        words = s.split()
        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)