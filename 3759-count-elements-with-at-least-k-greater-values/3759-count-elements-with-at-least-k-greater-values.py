class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == 0:
            return n

        nums.sort()

        # x qualifies iff at least k array elements are strictly greater.
        threshold = nums[n - k]
        return bisect_left(nums, threshold)