class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #brute force - rotate one step at time
        # time - Each rotation → O(n)
        #Done k times → O(n × k) 
        #Space - O(1)

        # n = len(nums)
        # k = k % n

        # for _ in range(k):
        #     last = nums[n - 1]

        #     for i in range(n - 1, 0, -1):
        #         nums[i] = nums[i - 1]

        #     nums[0] = last

        
        # Better - using extra array 
        # Time, space - O(n) - not in place 
        # n = len(nums)
        # k = k % n

        # temp = [0] * n

        # for i in range(n):
        #     temp[(i + k) % n] = nums[i]

        # for i in range(n):
        #     nums[i] = temp[i]

        n = len(nums)
        k = k % n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Step 1: reverse whole array
        reverse(0, n - 1)

        # Step 2: reverse first k elements
        reverse(0, k - 1)

        # Step 3: reverse remaining elements
        reverse(k, n - 1)
        #time - O(n)
        #space - O(1)