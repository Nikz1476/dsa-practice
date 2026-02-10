class Solution:
    def reverseVowels(self, s: str) -> str:
        #brute force
        # vowels = set("aeiouAEIOU")
        # chars = list(s)

        # # Step 1: collect vowels
        # vowel_list = [c for c in chars if c in vowels]

        # # Step 2: reverse vowels
        # vowel_list.reverse()

        # # Step 3: put them back
        # idx = 0
        # for i in range(len(chars)):
        #     if chars[i] in vowels:
        #         chars[i] = vowel_list[idx]
        #         idx += 1

        # return "".join(chars)
        
        #better 
        # vowels = set("aeiouAEIOU")
        # chars = list(s)
        # left, right = 0, len(chars) - 1

        # while left < right:
        #     while left < right and chars[left] not in vowels:
        #         left += 1
        #     while left < right and chars[right] not in vowels:
        #         right -= 1

        #     chars[left], chars[right] = chars[right], chars[left]
        #     left += 1
        #     right -= 1

        # return "".join(chars)

        #optimal 
        vowels = set("aeiouAEIOU")
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)

        #time,space - O(n) for all 