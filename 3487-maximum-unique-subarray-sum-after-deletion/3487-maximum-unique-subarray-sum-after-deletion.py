class Solution:
    def maxSum(self, nums):
        positive = set()

        for x in nums:
            if x > 0:
                positive.add(x)

        if positive:
            return sum(positive)

        return max(nums)