class Solution:
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        for i in range(len(nums)):
            if k and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        if k % 2:
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)