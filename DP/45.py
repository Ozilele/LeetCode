# Jump Game II problem
# https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums) -> int:
        if len(nums) == 1:
            return 0
        jumps = 1
        n = len(nums)
        currJump = nums[0]
        maxJump = nums[0]
        i = 0
        while i < n - 1:
            maxJump = max(maxJump, i + nums[i])

            if(i == currJump):
                jumps += 1
                currJump = maxJump
            i += 1
        return jumps