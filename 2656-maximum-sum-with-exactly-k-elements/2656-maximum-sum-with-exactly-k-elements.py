class Solution:
    def maximizeSum(self, nums, k):
        m = max(nums)
        return k * m + k * (k - 1) // 2