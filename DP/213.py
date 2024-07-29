# House Robber II
# https://leetcode.com/problems/house-robber-ii/

class Solution:

    def rob(self, nums) -> int:
        n = len(nums)
        if(n < 2):
            return nums[0]
        return max(self.max_robber(nums[0:n-1]), self.max_robber(nums[1:n]))

    # Formula - C(i) = max{C(i - 2) + nums[i], C(i - 1)}
    def max_robber(self, nums):
        amounts = [0] * (len(nums) + 1)
        curr = 2
        amounts[0] = 0
        amounts[1] = nums[0]

        for i in range(1, len(nums)):
            if(amounts[curr - 2] + nums[i] > amounts[curr - 1]):
                amounts[curr] = amounts[curr - 2] + nums[i]
            else:
                amounts[curr] = amounts[curr - 1]
            curr += 1
        return amounts[-1]
