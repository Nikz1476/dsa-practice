class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Both Methods - Time complexity - O(n)
                    #Space Complexity - O(1)
        #alternate
        #index = 0

        # Move non-zero elements forward
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[index] = nums[i]
        #         index += 1

        # Fill rest with zeros
        # for i in range(index, len(nums)):
        #     nums[i] = 0