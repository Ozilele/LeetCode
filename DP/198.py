# House Robber Problem
# https://leetcode.com/problems/house-robber/description/

class Solution:

    def rob(self, nums) -> int:
        totalAmount = 0
        amounts = [0] * (len(nums) + 1)
        amounts[0] = 0
        amounts[1] = nums[0]
        index = 2
        # C(i) - max money zebrana do i-tego domu
        # C(i) = max{C(i - 2) + nums[i], C(i - 1)}
        for i in range(1, len(nums)):
            if(amounts[index - 2] + nums[i] > amounts[index - 1]):
                amounts[index] = amounts[index - 2] + nums[i]
            else:
                amounts[index] = amounts[index - 1]
            index += 1
        return amounts[-1]
