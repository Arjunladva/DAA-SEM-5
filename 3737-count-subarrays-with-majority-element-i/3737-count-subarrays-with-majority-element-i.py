class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def add(self, i, value):
        while i < len(self.bit):
            self.bit[i] += value
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # target is majority iff transformed subarray has positive sum.
        prefix = [0]
        cur = 0

        for x in nums:
            cur += 1 if x == target else -1
            prefix.append(cur)

        values = sorted(set(prefix))
        bit = Fenwick(len(values))
        answer = 0

        for p in prefix:
            rank = bisect_left(values, p) + 1
            # Count previous prefix sums strictly smaller than p.
            answer += bit.query(rank - 1)
            bit.add(rank, 1)

        return answer
