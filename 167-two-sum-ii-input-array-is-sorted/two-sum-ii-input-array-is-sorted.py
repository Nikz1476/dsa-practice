class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # #BF   -  O(n^2), O(1)
        # n = len(numbers)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]

        # #O(n),O(n)
        # seen = {}
        
        # for  i,num in enumerate(numbers):
        #     need = target - num
        #     if need in seen:
        #         return [seen[need]+1,i+1]
        #     seen[num] = i


        #O(n),O(1)
        l = 0
        r = len(numbers) - 1
        for i in range(len(numbers)):
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r = r-1
            else:
                l = l+1
         