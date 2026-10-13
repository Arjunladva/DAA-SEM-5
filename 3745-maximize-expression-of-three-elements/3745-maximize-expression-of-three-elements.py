class Solution:
    def maximizeExpressionOfThree(self, nums):
        nums.sort()

        return nums[-1] + nums[-2] - nums[0]