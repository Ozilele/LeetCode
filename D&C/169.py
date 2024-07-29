# Majority Element Problem
# https://leetcode.com/problems/majority-element/description/

class Solution:

    def majorityElement(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        L = nums[:mid]
        R = nums[mid:]
        left_el = self.majorityElement(L)
        right_el = self.majorityElement(R)
        if left_el == right_el:
            return left_el
        else:
            left_count = 0
            right_count = 0
            for i in range(len(nums)):
                if nums[i] == left_el:
                    left_count += 1
                elif nums[i] == right_el:
                    right_count += 1
            if right_count > left_count:
                return right_el
            else:
                return left_el