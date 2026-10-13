class Solution:
    def smallestTrimmedNumbers(
        self, nums: List[str], queries: List[List[int]]
    ) -> List[int]:

        answer = []

        for k, trim in queries:
            order = sorted(
                range(len(nums)),
                key=lambda i: (nums[i][-trim:], i)
            )
            answer.append(order[k - 1])

        return answer