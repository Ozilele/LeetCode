# Reverse Pairs Problem
# https://leetcode.com/problems/reverse-pairs/description/

class Solution:

    def reversePairs(self, nums) -> int:
        count, arr = self.countReversePairs(nums, len(nums)) 
        return count
    
    def countReversePairs(self, nums, n):
        if n <= 1:
            return 0, [nums[0]] 
        mid = len(nums) // 2
        count_left, left_sorted = self.countReversePairs(nums[:mid], mid)
        count_right, right_sorted = self.countReversePairs(nums[mid:], n - mid)
        nums = left_sorted + right_sorted
        L = left_sorted
        R = right_sorted
        reverse_count = count_left + count_right
        j = mid

        for i in range(0, mid):
            while j < len(nums) and nums[i] > 2 * nums[j]:
                j += 1
            reverse_count += j - (mid)
        l = 0
        r = 0
        k = 0
        while l < len(L) and r < len(R):
            if L[l] <= R[r]:
                nums[k] = L[l]
                l += 1
            else:
                nums[k] = R[r]
                r += 1
            k += 1

        while l < len(L):
            nums[k] = L[l]
            l += 1
            k += 1
        while r < len(R):
            nums[k] = R[r]
            r += 1
            k += 1  
        return reverse_count, nums