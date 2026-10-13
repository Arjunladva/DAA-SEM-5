class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        for left in range(n):
            seen_even = set()
            seen_odd = set()

            for right in range(left, n):
                x = nums[right]

                if x % 2 == 0:
                    seen_even.add(x)
                else:
                    seen_odd.add(x)

                if len(seen_even) == len(seen_odd):
                    answer = max(answer, right - left + 1)

        return answer
