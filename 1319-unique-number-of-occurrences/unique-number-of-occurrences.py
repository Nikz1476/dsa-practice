class Solution:
    def uniqueOccurrences(self, arr):
        # Brute Force
        # Time complexity - O(n^2)
        # Space complexity - O(n)

        # freq = []

        # for i in range(len(arr)):
        #     count = 0
        #     for j in range(len(arr)):
        #         if arr[i] == arr[j]:
        #             count += 1
        #     freq.append(count)

        # # Check if any frequency repeats for different values
        # for i in range(len(freq)):
        #     for j in range(i + 1, len(freq)):
        #         if freq[i] == freq[j] and arr[i] != arr[j]:
        #             return False

        # return True


    # Method 2 - Better (hashmap + list)
    # Time Complexity- Counting → O(n)
    # Checking → O(k²) where k = number of unique elements (≤ n)

    # Worst case → O(n²)

    # Space Complexity- O(n) (dictionary)   
    # freq = {}

    #     # Count frequencies
    #     for num in arr:
    #         freq[num] = freq.get(num, 0) + 1

    #     values = list(freq.values())

    #     # Check if any frequency repeats
    #     for i in range(len(values)):
    #         for j in range(i + 1, len(values)):
    #             if values[i] == values[j]:
    #                 return False

    #     return True


    #Optimal - Hashmap + set
        freq = {}

        # Count occurrences
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        seen = set()

        for count in freq.values():
            if count in seen:
                return False
            seen.add(count)

        return True
