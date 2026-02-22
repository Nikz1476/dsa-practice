class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # #brute force, time - O(m+n log(m+n)), space - O(m+n)
        # arr = nums1 + nums2
        # arr.sort()

        # n = len(arr)
        # if n % 2 == 1:
        #     return arr[n // 2]
        # else:
        #     return (arr[n // 2 - 1] + arr[n // 2]) / 2


        # #better, time - O(m+n), space - O(1)
        # m, n = len(nums1), len(nums2)
        # total = m + n

        # i = j = 0
        # prev = curr = 0

        # for _ in range(total // 2 + 1):
        #     prev = curr

        #     if i < m and (j >= n or nums1[i] < nums2[j]):
        #         curr = nums1[i]
        #         i += 1
        #     else:
        #         curr = nums2[j]
        #         j += 1

        # if total % 2 == 1:
        #     return curr
        # else:
        #     return (prev + curr) / 2

        #optimal, time - O(log (m+n))
        # Always binary search smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (m + n + 1) // 2 - cut1

            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            right1 = float('inf') if cut1 == m else nums1[cut1]

            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right2 = float('inf') if cut2 == n else nums2[cut2]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)

            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1