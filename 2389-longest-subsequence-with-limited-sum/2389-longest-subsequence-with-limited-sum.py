class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        prefix = []
        total = 0
        for x in nums:
            total += x
            prefix.append(total)

        ans = []
        for q in queries:
            lo, hi = 0, len(prefix)
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] <= q:
                    lo = mid + 1
                else:
                    hi = mid
            ans.append(lo)
        return ans