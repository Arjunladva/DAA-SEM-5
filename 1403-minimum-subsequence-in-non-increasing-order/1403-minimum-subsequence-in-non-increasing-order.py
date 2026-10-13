class Solution:
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        remaining = sum(nums)
        cur = 0
        ans = []
        for x in nums:
            cur += x
            remaining -= x
            ans.append(x)
            if cur > remaining:
                break
        return ans