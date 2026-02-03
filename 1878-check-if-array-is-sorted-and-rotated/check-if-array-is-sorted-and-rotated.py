class Solution:
    def check(self, nums: List[int]) -> bool:
        #Method 1- Brute Force - O(n^2)
        #Idea:For every number, count how many times it appears by scanning the whole    array again. Then store these counts in a list and check if any two counts are equal.
        # freq = []

        # for i in range(len(arr)):
        #     count = 0
        #     for j in range(len(arr)):
        #         if arr[i] == arr[j]:
        #             count += 1
        #     freq.append(count)

        # # check if any frequency repeats
        # for i in range(len(freq)):
        #     for j in range(i+1, len(freq)):
        #         if freq[i] == freq[j] and arr[i] != arr[j]:
        #             return False

        # return True

#         Method - 2 - O(n)/ O(n^2 in worst case)
#         Idea:Count each number once using a hashmap (dictionary). Then compare frequencies.
#         freq = {}

#         for num in arr:
#             if num in freq:
#                 freq[num] += 1
#             else:
#                 freq[num] = 1

#         counts = list(freq.values())

#         for i in range(len(counts)):
#             for j in range(i+1, len(counts)):
#                 if counts[i] == counts[j]:
#                     return False

#         return True 


#Method 3 - optimal - 
# Idea:
# Count occurrences using dictionary
# Put counts in a set (sets keep only unique values)
# Compare lengths

        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False

        return True