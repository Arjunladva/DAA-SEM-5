class Solution:
    def maxKDistinct(self, nums, k):
        nums = sorted(set(nums), reverse=True)

        return nums[:k]