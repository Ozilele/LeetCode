# Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.Return true if you can reach the last index, or false otherwise.
# https://leetcode.com/problems/jump-game/description/ 

class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        currJump = nums[0]
        maxJump = nums[0]
        i = 0
        while i < n - 1:
            maxJump = max(maxJump, i + nums[i])
            if maxJump == i:
                return False
            if i + nums[i] >= n - 1:
                return True
            i += 1
        return False