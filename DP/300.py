# Longest Increasing Subsequence Problem
# https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:

    def lengthOfLIS(self, nums) -> int:
        return self.lengthLIS(nums, 0, len(nums)-1)

    def binarySearch(self, sub, val):
        h1 = len(sub)-1
        l0 = 0
        while(l0 <= h1):
            mid = l0 + (h1 - l0) // 2
            if sub[mid] < val:
                l0 = mid + 1
            elif val < sub[mid]:
                h1 = mid - 1
            else:
                return mid
        return l0

    def lengthLIS(self, nums, l, r):
        sub = []
        for x in nums:
            pos = self.binarySearch(sub,x)
            if pos == len(sub):
                sub.append(x)
            else:
                sub[pos] = x
        return len(sub)
            

