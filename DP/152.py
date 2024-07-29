# Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

class Solution:

    def maxProduct(self, nums) -> int:
        # Max(i) - Max Product on Subarray found to index i - exclusive
        # Curr(0) = nums[0], Max(0) = nums[0]
        # Max(i) = max(Max(i-1), Curr(i))
        n = len(nums)
        Max = [0] * n
        Min = [0] * n
        Max[0] = nums[0]
        Min[0] = nums[0]
        currMax = nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                tmp = Min[i - 1]
                Min[i - 1] = Max[i - 1]
                Max[i - 1] = tmp
            Max[i] = max(nums[i], Max[i-1] * nums[i])
            Min[i] = min(nums[i], Min[i-1] * nums[i])
            currMax = max(currMax, Max[i])
        return currMax