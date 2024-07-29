# Maximum Subarray Problem
# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums) -> int:
        return self.maxSubArrayUtil(nums, 0, len(nums) - 1)

    def maxSubArrayUtil(self, nums, l, r):
        if l >= r:
            return nums[l]
        mid = l + (r - l) // 2
        maxSumLeft = self.maxSubArrayUtil(nums, l, mid)
        maxSumRight = self.maxSubArrayUtil(nums, mid + 1, r)
        maxSum = max(maxSumLeft, maxSumRight)
        # check Sum between [l', mid - 1], mid, [mid + 1, r'] where l' >= l, r' <= r
        maxSubLeft = -10000000000000
        currSubLeft = 0
        maxSubRight = -10000000000000
        currSubRight = 0
        for k in range(mid - 1, l - 1, -1):
            # currSubLeft = max(nums[k], currSubLeft + nums[k])
            currSubLeft += nums[k]
            if currSubLeft > maxSubLeft:
                maxSubLeft = currSubLeft
        for j in range(mid + 1, r + 1):
            currSubRight += nums[j]
            if currSubRight > maxSubRight:
                maxSubRight = currSubRight

        sumWithMid = max(maxSubLeft + nums[mid] + maxSubRight, nums[mid] + maxSubRight)
        print(sumWithMid)
        return max(sumWithMid, maxSum)

